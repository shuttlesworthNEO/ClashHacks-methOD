import numpy as np
import pandas as pd
import theano
from keras.layers import Dense
from keras.models import Model,load_model

def decrypto(x):

	decoder = load_model("encoder.h5")

	x_ = list(x)
	
	inp = []
	inpu=[]
	for ix in range(len(x_)):
    	if ix%2==0:
        	inp.append(x_[ix])
	
	for ix in range(len(inp)):
		inpu.append(int(inp[ix], 16))

	y = np.array(tuple(inpu))

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

	dec_key=""
	for ix in inp:
		dec_key += str(ix)
	
	if crypt_str == x :
		return dec_key