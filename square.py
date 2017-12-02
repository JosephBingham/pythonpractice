#!/usr/bin/python
print "number: "
num = input()
i = 0.0
while(i**2 < num):
	i = i + 1

i = i - 1
n = 0
while(n < 1000000):
	i = (i + num/i)/2.0
	n = n + 1
#	if(n % 100000 == 0):
#		print i
print i, num**.5, i*i, num

