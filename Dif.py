#!/usr/bin/python
import math
n = 300; error = .5; y = .5; x = .5; h = 1.0
besth = 0; besty =0; beste = 10
for i in xrange(n):
	h *=.25
	y = (math.sin(x+h) - math.sin(x))/h
	temp = math.cos(x) - y
	error = temp if temp > 0 else -temp
	print "h ",h, "y", y,"error", error
	if(beste > error):
		besth = h
		beste = error
		besty = y

print "best run: ", "h ", besth, "y ", besty, "error ", beste
