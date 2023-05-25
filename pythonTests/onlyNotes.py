import numpy as np
from keras.models import Sequential, load_model
from keras.layers import LSTM, Dense, Dropout
import csv

# data = np.genfromtxt('csv-classical/1759.csv', delimiter=',')
# data = data[:, 3]

# X, y = [], []
# for i in range(len(data)-3):
#     X.append(data[i:i+3])
#     y.append(data[i+3])
# X, y = np.array(X), np.array(y)


# print("X.shape", X.shape)
# print("y.shape", y.shape)

# print("y", y)
# print("X", X)

# X = np.reshape(X, (X.shape[0], 3, 1))

# print("X.shape", X.shape)
# print("y.shape", y.shape)

# model = Sequential()

# model.add(LSTM(256, input_shape=(3, 1), return_sequences=True))
# model.add(Dropout(0.2))
# model.add(LSTM(256, return_sequences=True))
# model.add(Dropout(0.2))
# model.add(LSTM(256))
# model.add(Dropout(0.2))
# model.add(Dense(1, activation='linear'))
# model.compile(loss='mean_squared_error', optimizer='adam')

# # train LSTM model
# model.fit(X, y, epochs=500, verbose=2)



# model.save('first_model.h5')

loaded_model = load_model('first_model.h5')
# make predictions
start_notes = np.array([[63], [75], [48]]) # example input notes
generated_music = start_notes

for i in range(100): 
    x_input = np.reshape(generated_music[-3:], (1, 3, 1))
    y_pred = loaded_model.predict(x_input, verbose=0)
    next_note = int(y_pred)
    generated_music = np.vstack([generated_music, [next_note]])
    
print("generated_music", generated_music)










# model = Sequential()
# model.add(LSTM(256, input_shape=(3, 1), return_sequences=True))
# model.add(Dropout(0.2))
# model.add(LSTM(256, return_sequences=True))
# model.add(Dropout(0.2))
# model.add(LSTM(256))
# model.add(Dropout(0.2))
# model.add(Dense(3, activation='sigmoid'))

# # Compile the model
# model.compile(loss='mse', metrics=['mae'], optimizer='adam')

# # train LSTM model
# model.fit(X, y, epochs=100, batch_size=64)

# # make predictions
# x_input = np.array([[54],[72],[61]])
# x_input = np.reshape(x_input, (1, 3, 1))
# y_pred = model.predict(x_input)
# print(y_pred)