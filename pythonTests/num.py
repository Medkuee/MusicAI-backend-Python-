import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense

# define the input sequence
seq = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# create input/output pairs from the sequence

window_size = 3
X, y = [], []
for i in range(len(seq)-window_size):
    X.append(seq[i:i+window_size])
    y.append(seq[i+window_size])
X, y = np.array(X), np.array(y)

print("X", X.shape)
print("y", y.shape)

# reshape input data for LSTM model
X = np.reshape(X, (X.shape[0], window_size, 1))




# X, y = [], []
# for i in range(len(seq)-1):
#     X.append(seq[i])
#     y.append(seq[i+1])
# X, y = np.array(X), np.array(y)
# X = np.reshape(X, (X.shape[0], 1, 1))

# print("y.shape", y.shape)

# # reshape input data for LSTM model

# print("X", X)
# print("X.shape", X.shape)


# define LSTM model
# model = Sequential()
# model.add(LSTM(32, input_shape=(3, 1)))
# model.add(Dense(1, activation='linear'))
# model.compile(loss='mean_squared_error', optimizer='adam')

# # train LSTM model
# model.fit(X, y, epochs=10000, verbose=2)

# # make predictions
# x_input = np.array([[10],[20],[30]])
# x_input = np.reshape(x_input, (1, 3, 1))
# y_pred = model.predict(x_input, verbose=0)
# print(y_pred)
