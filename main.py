from SquenceBreaker import SequenceBreaker
import pandas as pd
import os
import numpy as np
import keras

# load a list of files into a 3D array of [samples, timesteps, features]
def load_file(filepath):
	dataframe = pd.read_csv(filepath)
	return dataframe.values




# get the labels
dirs = os.listdir('./ready')
d = dict(enumerate(dirs))
print(d)
x = []


# load file, remove the first(time index) and last column(nan)
loaded = load_file('./ges/recorded2.txt')
loaded = loaded[:,1:-1]
x.append(loaded)

# Standardize the data
from sklearn.preprocessing import StandardScaler
scalar = StandardScaler()
tran_x = []
for i in range(len(x)):
    scalar = scalar.fit(x[i])
    tran_x.append(scalar.transform(x[i]))
x = np.array(tran_x)


# count time
import timeit
start = timeit.default_timer()

# load Breaker
sb = SequenceBreaker()
x = sb.chop_data_into_frame_of_windowsize(np.array(x[0]))
x = sb.calc_var(x)
x = sb.seperate_gestures(x)

model = keras.models.load_model('./')

maxtimestep = 115

x_ls = []
for i in range(len(x)):
    if len(x[i]) < maxtimestep:
        difference = maxtimestep - len(x[i])
        d1 = difference//2
        d2 = difference - d1
        paddedx = np.concatenate([np.zeros((d1,30)),x[i], np.zeros((d2,30))], axis=0)
        x_ls.append( paddedx) 

y = model.predict(np.array(x_ls))
print(y)
for ys in y:
    print(d[np.argmax(ys)])
    

stop = timeit.default_timer()

print('Time: ', stop - start)  