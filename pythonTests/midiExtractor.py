import mido

# Load MIDI file
midi = mido.MidiFile('midi.midi')

# Loop through each track in the MIDI file
for i, track in enumerate(midi.tracks):
    print(f'Track {i + 1}:')

    # Loop through each message in the track
    for msg in track[:100]:
        print("msg", msg)
        # Check if the message is a note_on or note_off message
        if msg.type in ['note_on', 'note_off']:
            # Extract note number, velocity, and time from the message
            note_number = msg.note
            velocity = msg.velocity
            time = msg.time

            # Print the extracted note information
            # print(f'Note Number: {note_number}, Velocity: {velocity}, Time: {time}')
