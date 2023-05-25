import numpy as np 


# print(hello.files)

# np_load_old = np.load

# np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)
hello = np.load(file = "/Users/user/Downloads/cross-era_chords-chordino/musicnet.npz", allow_pickle=True, encoding='latin1')

# call load_data with allow_pickle implicitly set to true
# (train_data, train_labels), (test_data, test_labels) = hello.load_data(num_words=10000)
print(hello)
print(len(hello.files))
# print(hello["1788"])
# print(len(hello["1788"][0]))
# print(hello["1788"][0][0:1000])

# restore np.load for future normal usage
# np.load = np_load_old

