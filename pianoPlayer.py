import csv
import time
import midiutil
import sf2_loader
from midi2audio import FluidSynth
import numpy as np
from music21 import converter
from flask import Flask, request

# Create an instance of the Flask application
app = Flask(__name__)

output_path = "/Users/user/Desktop/Diploma/Music/src/screens/main/guest/guestFavoriteScreen/music-output/"

@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/create-music', methods=['POST'])
def submit_data():
    _data = request.json  
    print("data",_data)
    print("_data",_data["name"])

    with open('csv-classical/1759.csv', 'r') as file:
        reader = csv.reader(file)
        filtered_rows = []
        
        for row in reader:
            note = int(row[3])
            
            if note < 89:
                filtered_rows.append(row)

    # Load the piano soundfont
    soundfont_path = 'soundfonts/piano.SF2'

    # Create a MIDI file to store the piano notes
    midi_file = midiutil.MIDIFile(1)  # 1 track
    track = 0
    channel = 0
    # Iterate over the classical piece data and add the notes to the MIDI file
    for data in filtered_rows:
        # print("Data", data)
        start_time, end_time, _, note, _, _, _ = data
        velocity = 30  # Adjust the velocity as desired
        duration = (int(end_time) - int(start_time)) / 22500
        start_time = int(start_time) / 22500
        end_time = int(end_time) / 22500
        note = int(note)

        # Add the note to the MIDI file
        midi_file.addNote(
            track,
            channel,
            note,
            start_time,
            duration,
            velocity
        )

    # Save the MIDI file
    midi_filename = f'{output_path}{_data["name"]}.mid'
    with open(midi_filename, 'wb') as file:
        midi_file.writeFile(file)

    # Create an instance of FluidSynth with the SoundFont
    fluidsynth = FluidSynth(soundfont_path)

    # Convert MIDI to audio using FluidSynth
    # audio_file = 'output.wav'
    # fluidsynth.midi_to_audio(midi_filename, audio_file)

    # Convert Midi to mxl
    mxl_file_path = f'{output_path}{_data["name"]}.mxl'
    midi_stream = converter.parse(midi_filename)
    midi_stream.write('musicxml', fp=mxl_file_path)
    
    return 'Data submitted successfully'

app.run()
