for j in xrange(100):
	for i in xrange(100):
		if i % 5 == 0 or j % 5 == 0:
			print "*"
		if i % 20 == 0 or j % 20 == 0:
			print "\n"
		else:
			print " "

