#!/usr/bin/python
import random

#digits = input()

digits = 10
bad = 0
for i in xrange(100000):
	a = random.random()

	b = ((a*5)*a)**a

	c = ((10**digits)*b % (10**digits))

	d = (((2**digits)*b % (10**digits)) + c) % (10**digits)

	if c < 10**(digits-1):
#		print "non_satisfactory_key",int(c)
		bad = bad + 1
#	else:
#		print int(c)

print bad/100000.0
