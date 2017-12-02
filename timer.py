#!/usr/bin/python
from threading import Thread
import time

def timer(name, delay, repeat):
#	print "timer: " + name + " started"
	while repeat > 0:
		repeat -= 1
		time.sleep(delay)
		print name + ": " + str(time.ctime(time.time())
#	print "timer: " + name + "done"

def main(void):
	t1 = Thread(target=timer, args=("Timer1", 1, 5))
	t2 = Thread(target=timer, args=("Timer2", 2, 5))
	t1.start()
	t2.start()

#	print "main compleated"

if __name__ == "__main__":
	main()
