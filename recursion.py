#!/usr/bin/python
import sys


def factorialj(number):
	if number == 1:
		return 1
	else:
		return number * factorialj(number - 1)
	print number
def main():
	intputfile = ''
	outputfile = ''
	stuff = str(factorialj(int(sys.argv[1])))
	print factorialj(int(sys.argv[1])), "\n"
	print len(stuff)


if __name__ == '__main__':
	main()
