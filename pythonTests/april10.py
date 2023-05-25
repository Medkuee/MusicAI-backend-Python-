import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

data = np.genfromtxt('outputV2.csv', delimiter=',')
dataX = data[:, 3]
dataY = np.concatenate((data[:, :2] / 45000, np.array(data[:, 3])[:, np.newaxis]), axis=1)

X, y = [], []
for i in range(len(data)-3):
    X.append(dataY[i:i+3])
    y.append(dataY[i+3])
X, y = np.array(X), np.array(y)

# # Load and preprocess the music data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the input shape for each component
input_shape = (3, 3)

# Define the number of units in the LSTM layer
num_units_lstm = 64

# Create the LSTM model
model = Sequential()
model.add(LSTM(num_units_lstm, input_shape=input_shape))
model.add(Dense(3, activation='linear'))  # Output for predicted start_time, end_time, and note

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Train the model
model.fit(X_train, y_train, epochs=200, batch_size=64, validation_data=(X_test, y_test))

# Make predictions
start_notes = np.array([[0, 0.76, 63], [0, 0.76, 75], [0, 0.45,48]]) 

generated_music = start_notes

for i in range(100): 
    x_input = np.expand_dims(generated_music[-3:], axis=0)
    # print("generated_music[-3:]", generated_music[-3:])
    y_pred = model.predict(x_input, verbose=0)
    # print("y_pred", y_pred)
    generated_music = np.vstack([generated_music, y_pred])
    
print("generated_music", generated_music)
