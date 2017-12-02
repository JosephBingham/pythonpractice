#!/usr/bin/python
"""finding the area of a general space using only the boundry points
	this will only work for solid space as of now"""

print "points:"

raw_points = raw_input().split(' ')
points = []
if (len(raw_points) % 2 == 1):
	raise Exception('not a list of points')
else:
	for i in xrange(0,len(raw_points),2):
		points.append((int(raw_points[i]), int(raw_points[i+1])))

"""figure out how to count internal points"""
I = 0

area = len(points)/2.0 + I - 1

print points
print area



