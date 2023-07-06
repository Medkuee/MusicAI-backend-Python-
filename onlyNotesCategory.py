import numpy as np
# from keras.models import Sequential, load_model
# from keras.layers import LSTM, Dense, Dropout
import csv
import random
# import pygame
import time

# pygame.init()


# data = np.genfromtxt('csv-classical/1759.csv', delimiter=',')
data = np.genfromtxt('1759re.csv', delimiter=',')
data = data[:, 3]
data = [num for num in data if num < 88]


X, y = [], []
for i in range(len(data)-3):
    # print("data[i:i+3]", data[i:i+3])
    X.append(data[i:i+3])
    y.append(data[i+3])
X, y = np.array(X), np.array(y)


print("X.shape", X.shape)
print("y.shape", y.shape)

print("y", y)
print("X", X)

X = np.reshape(X, (X.shape[0], 3, 1))

print("X.shape", X.shape)
print("y.shape", y.shape)

# model = Sequential()

# model.add(LSTM(256, input_shape=(3, 1), return_sequences=True))
# model.add(Dropout(0.2))
# model.add(LSTM(256, return_sequences=True))
# model.add(Dropout(0.2))
# model.add(LSTM(256))
# model.add(Dropout(0.2))
# model.add(Dense(88, activation='softmax'))
# model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')

# # train LSTM model
# model.fit(X, y, epochs=200, verbose=2)



# model.save('first_modelREF.h5')

# loaded_model = load_model('first_modelREF.h5')
# # # make predictions
# start_notes = np.array([[74], [73], [74]]) # example input notes
# generated_music = start_notes

# for i in range(100): 
#     x_input = np.reshape(generated_music[-3:], (1, 3, 1))
#     y_pred = loaded_model.predict(x_input, verbose=0)
#     # print("y_pred", y_pred[0])
#     # print("Note: 1", np.argmax(y_pred))
#     sorted_indices = np.argsort(y_pred[0])
#     # print("NUMBERS", sorted_indices)
#     # print("NUMBERS", sorted_indices[-1:-6:-1])
#     # print("RANDOM", random.choice(sorted_indices[-1:-6:-1]))


#     # next_note = np.argmax(y_pred)
#     generated_music = np.vstack([generated_music, [random.choice(sorted_indices[-1:-4:-1])]])
    
# print("generated_music", generated_music)



# for file in generated_music:
#     print("HAHA", file[0])
#     pygame.mixer.music.load(f"mp3/{file[0]}.mp3")
#     pygame.mixer.music.play()

#     # Wait for 0.5 seconds
#     # random_number = random.uniform(0.3, 0.8)
#     # time.sleep(random_number)
#     time.sleep(0.5)

#     # Stop the audio playback
#     pygame.mixer.music.stop()

# pygame.quit()



# data = np.genfromtxt('1759re.csv', delimiter=',')
# data = data[:, 3]
# data = [num for num in data if num < 88]


# X, y = [], []
# for i in range(len(data)):
#     # print("data[i:i+3]", data[i:i+3])
#     X.append(data[i])
#     y.append(data[i])
# X, y = np.array(X), np.array(y)


# print("X.shape", X.shape)
# print("y.shape", y.shape)

# print("y", y)
# print("X", X)

# for file in y[:5]:
#     print("HAHA", int(file))
#     pygame.mixer.music.load(f"mp3/{int(file)}.mp3")
#     pygame.mixer.music.play()

#     # Wait for 0.5 seconds
#     # random_number = random.uniform(0.1, 0.5)
#     # time.sleep(random_number)
#     # time.sleep(0.5)

#     # Stop the audio playback
# time.sleep(20)
# pygame.mixer.music.stop()

# pygame.quit()