import time
from music21 import converter
from flask import Flask, request
import note_seq
from music21 import converter
from magenta.models.melody_rnn import melody_rnn_sequence_generator
from magenta.models.shared import sequence_generator_bundle
from note_seq.protobuf import generator_pb2
from note_seq.protobuf import music_pb2


# Create an instance of the Flask application
app = Flask(__name__)

output_path = "../MusicAI-mobile/src/screens/main/guest/guestFavoriteScreen/music-output/"

bundle = sequence_generator_bundle.read_bundle_file('models/lookback_rnn.mag')
generator_map = melody_rnn_sequence_generator.get_generator_map()
melody_rnn = generator_map['lookback_rnn'](checkpoint=None, bundle=bundle)
melody_rnn.initialize()

@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/create-music', methods=['POST'])
def submit_data():
    _data = request.json  
    music_create = music_pb2.NoteSequence()

    for data in _data["notes"]:
        note, duration, noteValue, startTime = data
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

    generator_options = generator_pb2.GeneratorOptions()
    generator_options.args['temperature'].float_value = temperature
    generate_section = generator_options.generate_sections.add(
    start_time=last_end_time + seconds_per_step,
    end_time=total_seconds)

    sequence = melody_rnn.generate(input_sequence, generator_options)
    midi_filename = f'{output_path}{_data["name"]}.mid'
    mxl_file_path = f'{output_path}{_data["name"]}.mxl'

    note_seq.sequence_proto_to_midi_file(sequence, midi_filename)

    midi_stream = converter.parse(midi_filename)
    midi_stream.write('musicxml', fp=mxl_file_path)
    
    return 'Data submitted successfully'

app.run()
