import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout

# Load the CSV dataset
data = np.genfromtxt('csv-classical/1759.csv', delimiter=',', usecols=(0, 1, 3, 6), dtype=[('start_time', 'i4'), ('end_time', 'i4'), ('note', 'i4'), ('note_value', 'U16')])
data = data[1:]

# Define the model architecture
model = Sequential()
model.add(LSTM(128, input_shape=(3, 2), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(128))
model.add(Dropout(0.2))
model.add(Dense(2))

# Compile the model
model.compile(loss='mse', optimizer='adam')

# Train the model
X_train = [(t[0], t[1], t[-1]) for t in data]
y_train = [t[2] for t in data]
# X_train = data[1:, -1:2]
# y_train = data[1:, 2]

# print("X_train", X_train)
# print("X_train", y_train)
model.fit(X_train, y_train, epochs=100, batch_size=64)

# # Generate music based on user input
# start_notes = np.array([[0.5, 0.5], [0.4, 0.6], [0.6, 0.4]]) # example input notes
# generated_music = start_notes

# for i in range(100): # generate 100 more notes
#     next_note = model.predict(np.array([generated_music[-3:]]))
#     generated_music = np.vstack([generated_music, next_note])
    
# print(generated_music)
