import numpy as np
from keras.models import Sequential, load_model, Model
from keras.layers import LSTM, Dense, Dropout, Input
import csv
import keras.backend as K
import tensorflow as tf

# Data preprocessing
data = np.genfromtxt('outputV3.csv', delimiter=',')
dataX = data[:, 3]
dataY = np.concatenate((data[:, :2] / 45000, np.array(data[:, 3])[:, np.newaxis]), axis=1)

X, y = [], []
for i in range(len(data)-3):
    X.append(dataY[i:i+3])
    y.append(dataY[i+3])
X, y = np.array(X), np.array(y)

print("X", X)
print("y", y)

# Model creation

# model = tf.keras.Sequential([
#     tf.keras.layers.Input(shape=(3,3)),
#     tf.keras.layers.Dense(88, activation='linear')
# ])

# model.compile(optimizer="adam", loss="mse")
# model.fit(X,y,epochs=5)


# model = Sequential()

# model.add(LSTM(256, input_shape=(3, 3), return_sequences=True))
# model.add(Dropout(0.2))
# model.add(LSTM(256, return_sequences=True))
# model.add(Dropout(0.2))
# model.add(LSTM(256))
# model.add(Dropout(0.2))

# model.add(Dense(3, activation='linear'))
# model.compile(loss="mse", optimizer='adam')

# X = np.reshape(X, (X.shape[0], 3, 3))
# y = np.reshape(y, (y.shape[0], 3))

# model.fit(X, y, epochs=30, verbose=2)

# model.save('fourth_model.h5')

# # Loading the model
loaded_model = load_model('third_model.h5')

# make predictions
start_notes = np.array([[0, 0.18, 67], [0.18, 0.13, 75], [0, 0.13,48]]) # example input notes
generated_music = start_notes

for i in range(1): 
    x_input = np.reshape(generated_music[-3:], (1, 3, 3))
    y_pred = loaded_model.predict(x_input)
    print("y_pred", y_pred)
    generated_music = np.vstack([generated_music, y_pred])
    
# print("generated_music", generated_music)

for i in generated_music:
    print(f"Start time: {round(i[0], 2)} End time: {round(i[1], 2)} note: {int(i[2])}")









# print("y_pred", y_pred)

# model.add(Dense(1, activation='sigmoid', name='start_time_output'))
# model.add(Dense(1, activation='sigmoid', name='end_time_output'))
# model.add(Dense(88, activation='softmax', name='note_output'))

# print("y", y)
# print("X", X)

# inputs = Input(shape=(3, 3))

# # Define the LSTM layer with 128 units
# lstm = LSTM(128)(inputs)

# model.compile(optimizer='adam', 
#               loss={'start_time_output':'binary_crossentropy',
#                     'end_time_output': 'binary_crossentropy',
#                     'note_output': 'categorical_crossentropy'},
#               metrics={'start_time_output': 'accuracy',
#                        'end_time_output': 'accuracy',
#                        'note_output': 'accuracy'})


# # Define the 3 output layers with 88 units each for the notes, start time, and end time
# start_time_output = Dense(1, activation='sigmoid', name='start_time_output')(lstm)
# end_time_output = Dense(1, activation='sigmoid', name='end_time_output')(lstm)
# note_output = Dense(88, activation='softmax', name='note_output')(lstm)
# # Define the model with 3 outputs
# model = Model(inputs=inputs, outputs=[start_time_output, end_time_output, note_output])
# model.add(Dense(3, activation='softmax'))

# # Compile the model with appropriate loss functions and metrics for each output
# model.compile(optimizer='adam', 
#               loss={'start_time_output':'binary_crossentropy',
#                     'end_time_output': 'binary_crossentropy',
#                     'note_output': 'categorical_crossentropy'},
#               metrics={'start_time_output': 'accuracy',
#                        'end_time_output': 'accuracy',
#                        'note_output': 'accuracy'})


# def custom_loss(y_true, y_pred):
#     mse1 = K.mean(K.square(y_pred[:, 0] - y_true[:, 0]))
#     mse2 = K.mean(K.square(y_pred[:, 1] - y_true[:, 1]))
#     mse3 = K.mean(K.square(y_pred[:, 2] - y_true[:, 2]))
#     return mse1 + mse2 + mse3