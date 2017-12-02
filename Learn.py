#!/usr/bin/python/

#def add_numbers(numone=1, numtwo=1):
#	return numone + numtwo

def add_number(*args):
	finalvalue = 0

	if args:
		for i in args:
			finalvalue += i
		return finalvalue
	else:
		return "Please Provide Numbers"
print add_number(50,60,60,50)

def createdict(**kvargs):
	for i in kvargs:
		print i, kvargs[i]
	return

createdict(Name='Derek',Age=35,YearBorn=1974)


# to change global variables, use global key word in a new declaration
# 	or use globals()['name'] =  function
#def main():
#	pass
	#will skip this method

#if ___name___ == '___main___': main()

#makes a main
