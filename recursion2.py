#!/usr/bin/python
import sys
import math
def main():
	intputfile = ''
	outputfile = ''
	stuff = str(math.factorial(int(sys.argv[1])))
	print math.factorial(int(sys.argv[1])), "\n"
	print len(stuff)


if __name__ == '__main__':
	main()
