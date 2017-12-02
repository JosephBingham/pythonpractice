#!/usr/bin/python

def is_prime(n):
	if n<2: return False
	else:
		for i in xrange(2, int(n**(.5))):
			if n % i == 0:
				return False
		return True

def largest_prime_factor(n):
	for i in xrange(int(n ** .5)/2*2+1, 3, -2):
		if n % i == 0 and is_prime(i):
			return i

def inclusion_exclusion(a,b,lim):
	def num(n):
		n = (n*(n+1))/2
		return n
	return a*(num((lim-a)/a))+b*(num((lim-b)/b))-a*b*(num((lim-a*b)/a*b))

def primes_sieve(limit):
    limitn = limit+1
    not_prime = set()
    primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i*2, limitn, i):
            not_prime.add(f)

        primes.append(i)

    return primes

#def genfib(n):
#	num =
