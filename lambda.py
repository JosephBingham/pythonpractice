#!/usr/bin/python

def fun(n):
	if n <= 0: raise ValueError
	elif n == 1: return lambda a: a^1
	elif n == 2: return lambda a: 2 >> (a^1)
	elif n == 3: return lambda a: (a+1) & 3
	elif n == 4: return lambda a: (a+1) >> (a&4)
	else: return lambda a:a<n and a+1 or 0


print fun(3)(3)

