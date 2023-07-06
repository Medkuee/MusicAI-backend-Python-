#%%
import numpy as np
from keras.models import Sequential, load_model
from keras.layers import LSTM, Dense, Dropout
import csv
import random
# import pygame
import time
import matplotlib.pyplot as plt

import pandas as pd

#%%
data = pd.read_csv("data.csv")

# print("data", data)

dataX = data.iloc[:, 0].values
dataY = data.iloc[:, 1].values

print("dataX", dataX)
print("dataY", dataY)

n_samples = 10

X, y = [], []
for i in range(len(data)-n_samples-1):
    X.append(dataX[i:i+n_samples])
    y.append(dataY[i+n_samples-1])
X, y = np.array(X), np.array(y)


print("X.shape", X.shape)
print("y.shape", y.shape)

print("y", y)
print("X", X)

X = np.reshape(X, (X.shape[0], n_samples, 1))

print("X.shape", X.shape)
print("y.shape", y.shape)
#%%
model = Sequential()

model.add(LSTM(256, input_shape=(10, 1), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(256, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(256))
model.add(Dropout(0.2))
model.add(Dense(1, activation='linear'))
model.compile(loss='mean_squared_error', optimizer='adam')

# train LSTM model
model.fit(X, y, epochs=200, verbose=2)

model.save('first_modelREF.h5')

#%%
data = pd.read_csv("test.csv")
dataX = data.iloc[:, 0].values
dataY = data.iloc[:, 1].values


n_samples = 10
y_jinken = []
jinken_x = []

X, y = [], []
for i in range(len(data)-n_samples-1):
    X.append(dataX[i:i+n_samples])
    jinken_x.append(dataX[i+n_samples-1])
    y_jinken.append(dataY[i+n_samples-1])
X = np.array(X)
X = np.reshape(X, (X.shape[0], n_samples, 1))

loaded_model = load_model('first_modelREF.h5')



for _data in X:
    pog = np.reshape(_data, (1, 10, 1))
    # print("pog", pog.shape)
    y_pred = loaded_model.predict(pog, verbose=0)
    # print("y_pred", y_pred)
    y.append(y_pred[0][0])

y = np.array(y)
y_jinken = np.array(y_jinken)
jinken_x = np.array(jinken_x)


print("y.shape", y.shape)
print("y_jinken.shape", y_jinken.shape)
print("jinken_x.shape", jinken_x.shape)

plt.plot(jinken_x, color = "blue")
plt.plot(y, color = "green")
plt.plot(y_jinken, color = "red")
plt.show()



# %%
