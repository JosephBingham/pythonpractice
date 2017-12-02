#!/usr/bin/python
import numpy as np

data = np.arange(1,1000001)

np.random.shuffle(data)

striny = ""
for i in data:
	striny += chr(i%256)

print striny
