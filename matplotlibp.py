#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)

x = []
max = 0
for i in xrange(101):
	k = (np.random.random())
	x.append(k)
	if k > max:
		max = k

y = [l**2 for l in x]
z = [l**3 for l in x]

plt.plot(x, y, 'ro')
plt.axis([0, max, 0, max**2])
plt.show()


