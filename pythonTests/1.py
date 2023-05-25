import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout

# Load the CSV dataset
# data = np.genfromtxt('csv-classical/1759.csv', delimiter=',')
data = np.genfromtxt('csv-classical/1759.csv', delimiter=',', usecols=(0, 1, 3), dtype=int)
data = data[1:]

# Normalize the data
# data[0:3] /= np.max(data[0:3])

# Define the model architecture
model = Sequential()
model.add(LSTM(128, input_shape=(3, 3), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(128))
model.add(Dropout(0.2))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam')

# Train the model
X_train = data[:2]
y_train = data[2]
print("X_train", X_train)
print("X_train", y_train)
# model.fit(X_train, y_train, epochs=100, batch_size=64)

# # Generate music based on user input
# start_notes = np.array([[0.5, 0.5, 60], [0.4, 0.6, 62], [0.6, 0.4, 64]]) # example input notes
# generated_music = start_notes

# for i in range(100): # generate 100 more notes
#     next_note = model.predict(np.array([generated_music[-3:]]))
#     generated_music = np.vstack([generated_music, np.array([0, 0, int(next_note[0][0] * 88)])])
    
# print(generated_music)


