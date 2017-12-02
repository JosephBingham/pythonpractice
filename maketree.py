#!/usr/bin/python
import math
print "size: "
size = input()
for i in xrange(size):
	if(i % 2 == 1):
		print " " * int(math.ceil(size-i/2.0)), "*" * i, " " * int(math.ceil(size-i/2.0))
	if(i == 1):
		final = (" " * int(math.ceil(size-i/2.0)), "*" * i, " " * int(math.ceil(size-i/2.0)))
	if(i == 5):
		fin = (" " * int(math.ceil(size-i/2.0)), "*" * i, " " * int(math.ceil(size-i/2.0)))
real = " "
finaltext = " "
for f in final:
	finaltext += f

for g in fin:
	real += g

print finaltext
print finaltext
print real
