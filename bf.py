#!/usr/bin/python

""" this is a brainf*** interpreter"""

print "input path: "

filename = raw_input()

print "approxomate tape size:"

tape_size = input()

file = open(filename, 'r')

tape = [0] * tape_size


#print tape

def exicute(line):
	i = 0
	while (i < len(line)):
		ch = line[i]
		if( ch == '+' ):
			tape[index] += 1
		elif( ch == '-' ):
			tape[index] -= 1
		elif( ch == '>' ):
			if(index < tape_size - 1):
				index += 1
			else:
				print "tape length added at end"
				tape.append(0)
				index += 1
		elif( ch == '<' ):
			if(index == 0):
				print "tape length added at beginning"
				tape.insert(0, 0)
			else:
				index -= 1
		elif( ch == '[' ):
			stringy = ""
			while( not  line[i] == ']' ):
				stringy += line[i]
				i += 1
			while( not tape[index] == 0):
				exicute(stringy)

		elif( ch == '.' ):
			print "input please"
			var = raw_input()
			tape[index] = var
		elif( ch == ',' ):
			print chr(tape[index])
		i += 1

index = 0

for line in file:
	exicute(line)
