import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
import csv

# def load_data(filename):
#     with open(filename, 'r') as csvfile:
#         reader = csv.reader(csvfile)
#         next(reader)  # skip header row
#         data = []
#         for row in reader:
#             start_time, end_time, note_value, note = row
#             data.append([float(start_time), float(end_time), int(note_value), int(note)])
#     return data
# data = load_data("music_data.csv")


# Load the CSV dataset
# data = np.genfromtxt('music_data.csv', delimiter=',')
data = np.genfromtxt('csv-classical/1759.csv', delimiter=',')

# Split the dataset into input and output sequences
X = data[:, :3]
y = data[:, 3]

# X = X.reshape((X.shape[0], 3, 2))

# print("X", X)
print("data", data.shape)
# print("y", y)

# print("X.shape", X.shape)
# print("y.shape", y.shape)

# Normalize the input data
# X_norm = X / 88.0
# X_norm = X 
# y = y / 88.0
# # X_norm = np.expand_dims(X / 88.0, axis=0)
# X_norm = np.reshape(X_norm, (X_norm.shape[0], X_norm.shape[1], 1))

# print("y", y)
# print("y.shape", y.shape)
# print("X_norm", X_norm)
# print("X_norm.shape", X_norm.shape)


# # Define the model architecture
# model = Sequential()
# model.add(LSTM(256, input_shape=(3, 1), return_sequences=True))
# model.add(Dropout(0.2))
# model.add(LSTM(256, return_sequences=True))
# model.add(Dropout(0.2))
# model.add(LSTM(256))
# model.add(Dropout(0.2))
# model.add(Dense(1, activation='sigmoid'))

# # Compile the model
# model.compile(loss='binary_crossentropy', optimizer='adam')

# # Train the model
# model.fit(X_norm, y, epochs=10, batch_size=64)

# # Generate music based on user input
# start_notes = np.array([[63], [75], [48]]) # example input notes
# generated_music = start_notes

# print("generated_music[-3:]", generated_music[-3:])
# # print("X_norm", X_norm)
# # print("start_notes", start_notes)
# # print("start_notes.shape", start_notes.shape)


# for i in range(10): # generate 100 more notes
#     X_input = np.expand_dims(generated_music[-3:] / 88.0, axis=0)
#     print("X_input", X_input)
#     print("X_input.shape", X_input.shape)
#     y_pred = model.predict(X_input)
#     # y_pred = model.predict(generated_music[-3:])
#     # print("y_pred", y_pred)
#     next_note = int(y_pred * 88)
#     # print("next_note", next_note)
#     # print("generated_music", generated_music)
#     generated_music = np.vstack([generated_music, [next_note]])
    
# print("generated_music", generated_music)
