#!/usr/bin/python

vowels = ['a', 'e', 'i', 'o', 'u']
print "string: "
stringy = raw_input()

letters = list(stringy)

count = 0
for l in letters:
	if l in vowels:
		count += 1

print count
