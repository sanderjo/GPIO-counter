#!/usr/bin/env python

import RPi.GPIO as GPIO
import datetime
import sys
import signal

#verbose = True		# global variable

############################################################################################################
############################################################################################################

def printusage(progname):
        print progname + ' <gpio-pin-number> <filename> [debug]'
        print 'Example usage: ' 
	print progname + ' 23 /path/to/mylogfile'
        print progname + ' 23 /path/to/mylogfile debug'
	sys.exit(-1)

def signal_handler(signal, frame):
        if verbose:
		print('You pressed Ctrl+C, so exiting')
	GPIO.cleanup()
        sys.exit(0)


def readvalue(myworkfile):
	try:
		f = open(myworkfile, 'ab+')		# open for reading. If it does not exist, create it
		value = int(f.readline().rstrip())	# read the first line; it should be an integer value
	except:
		value = 0				# if something went wrong, reset to 0
	#print "old value is", value
	f.close()	# close for reading
	return value


def writevalue(myworkfile,value):
	f = open(myworkfile, 'w')
	f.write((str(value)+ '\n'))			# the value
	f.write((str(datetime.datetime.now())+ '\n'))	# timestamp
	f.close()	

############################################################################################################
############################################################################################################

######### Initialization


#### get input parameters:

try:
	mygpiopin = int(sys.argv[1])
	logfile = sys.argv[2]
except:
	printusage(sys.argv[0])

verbose = False
try:
	if sys.argv[3] == 'debug':
		verbose = True
		print "Verbose is On"
	else:
		printusage(sys.argv[0])
except:
	pass

#### if verbose, print some info

verbose = True

if verbose:
	print "GPIO is " + str(mygpiopin)
	print "Logfile is " + logfile
	print "Current value is " + str(readvalue(logfile))


#### setup

GPIO.setmode(GPIO.BCM)
GPIO.setup(mygpiopin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

signal.signal(signal.SIGINT, signal_handler)	# SIGINT = interrupt by CTRL-C


########## Main Loop 

while True:
	# wait for pin going up
	GPIO.wait_for_edge(mygpiopin, GPIO.RISING)

	# read value from file
	counter=readvalue(logfile) + 1
	if verbose:
		print "New value is", counter

	# write value to file
	writevalue(logfile,counter)

	# and wait for pin going down
	GPIO.wait_for_edge(mygpiopin, GPIO.FALLING)

############################################################################################################
############################################################################################################



