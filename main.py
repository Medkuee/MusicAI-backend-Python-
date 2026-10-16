import os
import re
import math
import time
from music21 import converter
from flask import Flask, request
import note_seq
from music21 import converter
from dotenv import load_dotenv
from magenta.models.melody_rnn import melody_rnn_sequence_generator
from magenta.models.shared import sequence_generator_bundle
from note_seq.protobuf import generator_pb2
from note_seq.protobuf import music_pb2

load_dotenv()

# Create an instance of the Flask application
app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Generated files are written into the mobile app so its WebView pages can load them.
# Relative paths are resolved from this folder, not from where the script is started.
output_path = os.path.join(
    BASE_DIR,
    os.getenv("OUTPUT_DIR", "../MusicAI-mobile/src/screens/main/guest/guestFavoriteScreen/music-output/"),
)

# The mobile app sends the saved music id as the name, e.g. "14"
NAME_PATTERN = re.compile(r'^[A-Za-z0-9_-]{1,64}$')
MAX_NOTES = 100

bundle = sequence_generator_bundle.read_bundle_file(os.path.join(BASE_DIR, 'models/lookback_rnn.mag'))
generator_map = melody_rnn_sequence_generator.get_generator_map()
melody_rnn = generator_map['lookback_rnn'](checkpoint=None, bundle=bundle)
melody_rnn.initialize()


def is_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def validate_request(_data):
    """Returns an error message, or None if the request body looks valid."""
    if not isinstance(_data, dict):
        return 'Request body must be JSON'

    name = _data.get("name")
    if not isinstance(name, str) or not NAME_PATTERN.fullmatch(name):
        return 'name must be 1-64 letters, numbers, "-" or "_"'

    notes = _data.get("notes")
    if not isinstance(notes, list) or not 0 < len(notes) <= MAX_NOTES:
        return f'notes must be a list of 1-{MAX_NOTES} notes'

    for data in notes:
        if not isinstance(data, dict):
            return 'each note must be an object'
        # note is the piano key index (0-87), startTime is in ms, duration in seconds
        if not is_number(data.get("note")) or int(data["note"]) != data["note"] or not 0 <= data["note"] <= 87:
            return 'note must be a whole number between 0 and 87'
        if not is_number(data.get("startTime")) or data["startTime"] < 0:
            return 'startTime must be a number >= 0'
        if not is_number(data.get("duration")) or data["duration"] < 0:
            return 'duration must be a number >= 0'

    return None


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/create-music', methods=['POST'])
def submit_data():
    _data = request.get_json(silent=True)
    error = validate_request(_data)
    if error:
        return {'error': error}, 400

    if not os.path.isdir(output_path):
        return {'error': f'Output folder not found: {output_path}'}, 500

    music_create = music_pb2.NoteSequence()

    for data in _data["notes"]:
        note = int(data["note"]) + 21
        start_time = data["startTime"] / 1000
        end_time = start_time + data["duration"]
        music_create.notes.add(pitch=note, start_time=start_time, end_time=end_time, velocity=80)
        print(start_time, end_time)
    music_create.total_time = _data["notes"][-1]["duration"] + (_data["notes"][-1]["startTime"] / 1000)

    music_create.tempos.add(qpm=60)

    input_sequence = music_create
    num_steps = 512
    temperature = 1.0

    last_end_time = (max(n.end_time for n in input_sequence.notes)
                    if input_sequence.notes else 0)
    qpm = input_sequence.tempos[0].qpm
    seconds_per_step = 60.0 / qpm / melody_rnn.steps_per_quarter
    total_seconds = num_steps * seconds_per_step

    print("total_seconds", total_seconds)

    if last_end_time + seconds_per_step >= total_seconds:
        return {'error': 'Recording is too long to continue'}, 400

    generator_options = generator_pb2.GeneratorOptions()
    generator_options.args['temperature'].float_value = temperature
    generate_section = generator_options.generate_sections.add(
    start_time=last_end_time + seconds_per_step,
    end_time=total_seconds)

    sequence = melody_rnn.generate(input_sequence, generator_options)
    midi_filename = os.path.join(output_path, f'{_data["name"]}.mid')
    mxl_file_path = os.path.join(output_path, f'{_data["name"]}.mxl')

    note_seq.sequence_proto_to_midi_file(sequence, midi_filename)

    midi_stream = converter.parse(midi_filename)
    midi_stream.write('musicxml', fp=mxl_file_path)

    return 'Data submitted successfully'

if __name__ == '__main__':
    app.run()
