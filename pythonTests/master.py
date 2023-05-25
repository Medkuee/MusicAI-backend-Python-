import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
import csv

data = np.genfromtxt('csv-classical/1759.csv', delimiter=',')

with open('csv-classical/1759.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    y = [[int(row[0]), int(row[1]), int(row[3])] for row in reader]

y = np.array(y)
y = y[3:,:]
X = data[:, 3]
X_data = []
for i in range(len(X)-3):
    X_data.append(X[i:i+3])
X_data = np.array(X_data)
X = np.reshape(X_data, (X_data.shape[0], 3, 1))

# print("X.shape", X.shape)
# print("y.shape", y.shape)

# print("y", y)
# print("X", X)

model = Sequential()
model.add(LSTM(256, input_shape=(3, 1), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(256, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(256))
model.add(Dropout(0.2))
model.add(Dense(3, activation='sigmoid'))

# Compile the model
model.compile(loss='mse', metrics=['mae'], optimizer='adam')

# train LSTM model
model.fit(X, y, epochs=100, batch_size=64)

# make predictions
x_input = np.array([[54],[72],[61]])
x_input = np.reshape(x_input, (1, 3, 1))
y_pred = model.predict(x_input)
print(y_pred)