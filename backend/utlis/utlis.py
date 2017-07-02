import numpy as np
import pandas as pd
import theano
from keras.layers import Dense
from keras.models import Model,load_model
from crypt import crypto
from decrypt import decrypto

def check(x):

	if len(x) == 16:
		func_ = crypto(x)
	elif len(x) == 32:
		func_ = decrypto(x)
	else:	
		func_ = "Sorry you entered invalid data"
	
	return func_	