import midiutil
import csv

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

print("filtered_rows", len(filtered_rows[:10]))
for data in filtered_rows[:10]:
    # print("Data", data)
    start_time, end_time, _, note, _, _, _ = data
    velocity = 30  # Adjust the velocity as desired
    duration = (int(end_time) - int(start_time)) / 22500
    start_time = int(start_time) / 22500
    end_time = int(end_time) / 22500
    note = int(note)
    print(start_time, end_time)