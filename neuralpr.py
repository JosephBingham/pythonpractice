#!/usr/bin/python
import numpy as np

def nonlin(x, deriv=False):
	"""for back propagation"""
	if(deriv):
		return x*(1-x)
	
	return 1/(1+np.exp(-1*x))


x = np.array([[0,0,1], [0,1,1], [1,0,1] [1,1,1]])
y = np.array([[0], [1], [1], [0]])

np.random.seed(1)

			#matrix	  #the one is a bias	
syn0 = 2*np.random.random((3,4)) - 1
syn1 = 2*np.random.random((4,1)) - 1

#training







