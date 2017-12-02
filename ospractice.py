#!/usr/bin/python
import logging, os

os.chdir("/home/joseph")
#print os.getcwd()

logname = "example.log"

#logging.basicConfig(filename=logname,level=logging.DEBUG)

#logging.debug('This message should go to the log file')
#logging.debug('this is an update')
logging.basicConfig(filename=logname, level=logging.DEBUG)

logging.info('\ntest')





