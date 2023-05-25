# # from note_seq.protobuf import music_pb2
# import note_seq
# from music21 import converter



# # note_seq.sequence_proto_to_midi_file(twinkle_twinkle, 'loolol_output.mid')

# # Import dependencies.
# from magenta.models.melody_rnn import melody_rnn_sequence_generator
# from magenta.models.shared import sequence_generator_bundle
# from note_seq.protobuf import generator_pb2
# from note_seq.protobuf import music_pb2

# import midiutil
# import csv

# with open('csv-classical/1759.csv', 'r') as file:
#     reader = csv.reader(file)
#     filtered_rows = []
    
#     for row in reader:
#         note = int(row[3])
        
#         if note < 89:
#             filtered_rows.append(row)

# # Load the piano soundfont
# soundfont_path = 'soundfonts/piano.SF2'

# # Create a MIDI file to store the piano notes
# midi_file = midiutil.MIDIFile(1)  # 1 track
# track = 0
# channel = 0
# # Iterate over the classical piece data and add the notes to the MIDI file
# twinkle_twinkle = music_pb2.NoteSequence()

# # print("filtered_rows", len(filtered_rows[:10]))
# # for data in filtered_rows[:10]:
# #     # print("Data", data)
# #     start_time, end_time, _, note, _, _, _ = data
# #     velocity = 30  # Adjust the velocity as desired
# #     duration = (int(end_time) - int(start_time)) / 22500
# #     start_time = int(start_time) / 22500
# #     end_time = int(end_time) / 22500
# #     note = int(note)
# #     twinkle_twinkle.notes.add(pitch=note, start_time=start_time, end_time=end_time, velocity=80)

# #     print(start_time, end_time)

# # Initialize the model.
# print("Initializing Melody RNN...")
# bundle = sequence_generator_bundle.read_bundle_file('lookback_rnn.mag')
# generator_map = melody_rnn_sequence_generator.get_generator_map()
# melody_rnn = generator_map['lookback_rnn'](checkpoint=None, bundle=bundle)
# melody_rnn.initialize()

# print('🎉 Done!')


# # # Add the notes to the sequence.
# twinkle_twinkle.notes.add(pitch=75+9, start_time=0.0, end_time=0.25, velocity=80)
# twinkle_twinkle.notes.add(pitch=74+9, start_time=0.25, end_time=0.5, velocity=80)
# twinkle_twinkle.notes.add(pitch=75+9, start_time=0.5, end_time=0.75, velocity=80)
# twinkle_twinkle.notes.add(pitch=76+9, start_time=0.75, end_time=1, velocity=80)
# twinkle_twinkle.notes.add(pitch=75+9, start_time=1, end_time=1.25, velocity=80)
# twinkle_twinkle.notes.add(pitch=74+9, start_time=1.25, end_time=1.5, velocity=80)
# twinkle_twinkle.notes.add(pitch=75+9, start_time=1.5, end_time=1.75, velocity=80)
# twinkle_twinkle.notes.add(pitch=76+9, start_time=1.75, end_time=2, velocity=80)
# twinkle_twinkle.notes.add(pitch=78+9, start_time=2.0, end_time=2.25, velocity=80)
# twinkle_twinkle.notes.add(pitch=77+9, start_time=2.25, end_time=2.5, velocity=80)
# twinkle_twinkle.notes.add(pitch=76+9, start_time=2.5, end_time=2.75, velocity=80)
# twinkle_twinkle.total_time = 3

# twinkle_twinkle.tempos.add(qpm=60)

# # Model options. Change these to get different generated sequences! 

# input_sequence = twinkle_twinkle # change this to teapot if you want
# num_steps = 512 # change this for shorter or longer sequences
# temperature = 1.0 # the higher the temperature the more random the sequence.

# # Set the start time to begin on the next step after the last note ends.
# last_end_time = (max(n.end_time for n in input_sequence.notes)
#                   if input_sequence.notes else 0)
# qpm = input_sequence.tempos[0].qpm 
# seconds_per_step = 60.0 / qpm / melody_rnn.steps_per_quarter
# total_seconds = num_steps * seconds_per_step

# print("total_seconds", total_seconds)

# generator_options = generator_pb2.GeneratorOptions()
# generator_options.args['temperature'].float_value = temperature
# generate_section = generator_options.generate_sections.add(
#   start_time=last_end_time + seconds_per_step,
#   end_time=total_seconds)

# # Ask the model to continue the sequence.
# sequence = melody_rnn.generate(input_sequence, generator_options)

# note_seq.sequence_proto_to_midi_file(sequence, 'lookback_output.mid')

# midi_stream = converter.parse("lookback_output.mid")
# midi_stream.write('musicxml', fp="lookback_output.mxl")
# # note_seq.plot_sequence(sequence)
# # note_seq.play_sequence(sequence, synth=note_seq.fluidsynth)


# from note_seq.protobuf import music_pb2
# import note_seq
# # Import dependencies.
# from magenta.models.music_vae import configs
# from magenta.models.music_vae.trained_model import TrainedModel
# twinkle_twinkle = music_pb2.NoteSequence()

# # Add the notes to the sequence.
# twinkle_twinkle.notes.add(pitch=60, start_time=0.0, end_time=0.5, velocity=80)
# twinkle_twinkle.notes.add(pitch=60, start_time=0.5, end_time=1.0, velocity=80)
# twinkle_twinkle.notes.add(pitch=67, start_time=1.0, end_time=1.5, velocity=80)
# twinkle_twinkle.notes.add(pitch=67, start_time=1.5, end_time=2.0, velocity=80)
# twinkle_twinkle.notes.add(pitch=69, start_time=2.0, end_time=2.5, velocity=80)
# twinkle_twinkle.notes.add(pitch=69, start_time=2.5, end_time=3.0, velocity=80)
# twinkle_twinkle.notes.add(pitch=67, start_time=3.0, end_time=4.0, velocity=80)
# twinkle_twinkle.notes.add(pitch=65, start_time=4.0, end_time=4.5, velocity=80)
# twinkle_twinkle.notes.add(pitch=65, start_time=4.5, end_time=5.0, velocity=80)
# twinkle_twinkle.notes.add(pitch=64, start_time=5.0, end_time=5.5, velocity=80)
# twinkle_twinkle.notes.add(pitch=64, start_time=5.5, end_time=6.0, velocity=80)
# twinkle_twinkle.notes.add(pitch=62, start_time=6.0, end_time=6.5, velocity=80)
# twinkle_twinkle.notes.add(pitch=62, start_time=6.5, end_time=7.0, velocity=80)
# twinkle_twinkle.notes.add(pitch=60, start_time=7.0, end_time=8.0, velocity=80) 
# twinkle_twinkle.total_time = 8

# twinkle_twinkle.tempos.add(qpm=60)


# # Here's another NoteSequence!
# teapot = music_pb2.NoteSequence()
# teapot.notes.add(pitch=69, start_time=0, end_time=0.5, velocity=80)
# teapot.notes.add(pitch=71, start_time=0.5, end_time=1, velocity=80)
# teapot.notes.add(pitch=73, start_time=1, end_time=1.5, velocity=80)
# teapot.notes.add(pitch=74, start_time=1.5, end_time=2, velocity=80)
# teapot.notes.add(pitch=76, start_time=2, end_time=2.5, velocity=80)
# teapot.notes.add(pitch=81, start_time=3, end_time=4, velocity=80)
# teapot.notes.add(pitch=78, start_time=4, end_time=5, velocity=80)
# teapot.notes.add(pitch=81, start_time=5, end_time=6, velocity=80)
# teapot.notes.add(pitch=76, start_time=6, end_time=8, velocity=80)
# teapot.total_time = 8

# teapot.tempos.add(qpm=60)





# # Initialize the model.
# print("Initializing Music VAE...")
# music_vae = TrainedModel(
#       configs.CONFIG_MAP['cat-drums_2bar_small'], 
#       batch_size=4, 
#       checkpoint_dir_or_path='pog.data-00000-of-00001')

# print('🎉 Done!')

# generated_sequences = music_vae.sample(n=2, length=80, temperature=1.0)

# for ns in generated_sequences:
#   print(ns)
#   # note_seq.plot_sequence(ns)
#   # note_seq.play_sequence(ns, synth=note_seq.fluidsynth)

# num_steps = 8

# # This gives us a list of sequences.
# note_sequences = music_vae.interpolate(
#       twinkle_twinkle,
#       teapot, 
#       num_steps=num_steps,
#       length=32)

# # Concatenate them into one long sequence, with the start and 
# # end sequences at each end. 
# interp_seq = note_seq.sequences_lib.concatenate_sequences(note_sequences)

# note_seq.sequence_proto_to_midi_file(interp_seq, 'drums_sample_output.mid')

