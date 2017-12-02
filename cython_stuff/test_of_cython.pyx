
cpdef long int fib(int n):
	cdef long int x = 1, i = 2
	while i <= n and x*i > 0:
		x *= i
		i += 1
	return x


