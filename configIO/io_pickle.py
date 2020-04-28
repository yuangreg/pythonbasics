import pickle

dict = {'scale': 1, 'x0': 2, 'y0': 3}

# Saving Parameters
file = open('params.pickle', 'wb')
pickle.dump(dict, file)
file.close()

# Loading Parameters
file = open('params.pickle', 'rb')
config = pickle.load(file)