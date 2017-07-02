import numpy as np
import pandas as pd
import theano
from keras.layers import Dense
from keras.models import Model,load_model
from utlis.crypt import crypto
from utlis.decrypt import decrypto

def check(x):

	if len(x) == 16:
		func_ = crypto(x)
	else if len(x) == 32:
		func_ = decrypto(x)

	return func_	