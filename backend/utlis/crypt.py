import numpy as np
import pandas as pd
import theano
from keras.layers import Dense
from keras.models import Model,load_model

def crypto(x):
	
	encoder = load_model("/home/vasu/all_projects/Hackathons/ClashHacks-methOD/backend/utlis/encoder.h5")

	x = list(x)
	
	for ix in range(len(x)):
		x[ix] = int(x[ix], 16)

	y = np.array(tuple(x))

	y = y.reshape(1,16)

	out = encoder.predict(y)
	out = out.reshape(32,1)

	cryto = []

	for ix in range(out.shape[0]):
		if ix%2==1:
			cryto.append(str(int(out[ix])))
		else:
			cryto.append(str(y[0][ix/2]))

	crypt_str = ""

	for ix in cryto:
		crypt_str += hex(int(ix)%16).split('x')[-1]

	print crypt_str
	return crypt_str