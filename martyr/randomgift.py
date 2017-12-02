#!/usr/bin/python
import random

print "enter <person>: <gift1>, <gift2> ..."

dicts = {}
gift_info = "start: start"
while not gift_info == "end: end":
	print "enter another person and gifts or 'end: end' to end"
	if not gift_info == "start: start":
		stringy = gift_info.split(': ')
		dicts[stringy[0]] = stringy[1].split(', ')
	gift_info = raw_input()

#for s in dicts:
#	print s, dicts[s]
name = "start"
print "name to be given gift"
while not name == "end":
	print "name or 'end' to end"
	if not name == "start":
		randomy = random.randint(0, len(dicts[name])-1)
		print dicts[name][randomy]
	name = raw_input()
