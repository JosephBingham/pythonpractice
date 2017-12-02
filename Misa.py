#!/usr/bin/python
import math
import operator as op
a = 2
b = 3
c = 2
t = 0

def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer // denom

for i in xrange(b + 1):
	for j in xrange(a + 1):
		d = ncr(a,j) * ncr(b,i) * math.factorial(i+j) * (b+c-1) * math.factorial(a + 2*b + c - i - j - 1)
		n = math.factorial(a + 2*b + c)
		t += float(d)/n


print t

