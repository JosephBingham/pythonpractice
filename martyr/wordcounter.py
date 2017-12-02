#!/usr/bin/python

print "string: "
worded = {}
stringy = raw_input()

wordy = stringy.split(" ")

for w in wordy:
	if not w in worded:
		worded[w] = 1
	else:
		worded[w] = worded[w] + 1

print worded

