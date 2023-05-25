import glob
import numpy as np
from music21 import converter, instrument, note, chord

# Step 1: MIDI Data Preprocessing
midi_files_path = "midis/*.mid"

notes = []
durations = []
for file in glob.glob(midi_files_path):
    midi = converter.parse(file)

    # Extract notes, chords, and their durations from MIDI file
    notes_to_parse = None
    parts = instrument.partitionByInstrument(midi)
    if parts:
        # Select notes from the first instrument part
        notes_to_parse = parts.parts[0].recurse()
    else:
        notes_to_parse = midi.flat.notes

    for element in notes_to_parse:
        if isinstance(element, note.Note):
            # Add individual notes and their durations to the notes and durations lists
            notes.append(str(element.pitch))
            durations.append(element.duration.quarterLength)
        elif isinstance(element, chord.Chord):
            # Add chord pitches as a string and their durations to the notes and durations lists
            notes.append('.'.join(str(n) for n in element.normalOrder))
            durations.append(element.duration.quarterLength)

# Step 2: Data Preparation
# Prepare the data for LSTM input

print("notes", notes)
print("durations", durations)
print("len notes", len(notes))
print("len durations", len(durations))

# Get all unique pitches (notes and chords)
# pitches = sorted(set(notes))

# # Create a mapping from pitch to integer value
# pitch_to_int = dict((pitch, idx) for idx, pitch in enumerate(pitches))

# # Convert the notes and durations to sequences of integers
# sequence_length = 100  # Adjust the sequence length as desired
# input_sequences = []
# output_sequences = []
# for i in range(0, len(notes) - sequence_length, 1):
#     sequence_in = notes[i:i + sequence_length]
#     sequence_out = notes[i + sequence_length]
#     input_sequences.append([pitch_to_int[pitch] for pitch in sequence_in])
#     output_sequences.append(pitch_to_int[sequence_out])

# # Convert the input sequences and durations to a numpy array
# num_sequences = len(input_sequences)
# input_sequences = np.reshape(input_sequences, (num_sequences, sequence_length, 1))
# input_durations = np.array(durations[:num_sequences])
# input_durations = np.reshape(input_durations, (num_sequences, sequence_length, 1))
# input_data = np.concatenate((input_sequences, input_durations), axis=2)
# input_data = input_data / float(len(pitches))  # Normalize the input

# # Convert the output sequences to a categorical format
# output_sequences = np.array(output_sequences)
# # output_sequences = to_categorical(output_sequences)

# # Split the data into training and validation sets
# train_size = int(0.8 * num_sequences)
# train_input = input_data[:train_size]
# train_output = output_sequences[:train_size]
# val_input = input_data[train_size:]
# val_output = output_sequences[train_size:]
