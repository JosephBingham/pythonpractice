#!/usr/bin/python
func = input("operation: (put o for options)")

add = (lambda x, y: x + y)
sub = (lambda x, y: x - y)
mult = (lambda x, y: x*y)
indiv = (lambda x, y: x/y)
div = (lambda x, y: float(x)/y)
expbase = (lambda x, y: x ** y)
nroot = (lambda x, y: x ** (1.0/y))
absolute = (lambda x: x if x > 0 else -x)


functions = ["add", "sub", "mult", "indiv", "div", "expbase", "nroot", "absolute"]

if func == 'o':
	for string in functions:
		print string, "/n"



#def evalpol( pol, x):

