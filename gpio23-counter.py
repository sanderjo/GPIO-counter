#!/usr/bin/env python

import RPi.GPIO as GPIO
import datetime
import sys
import signal

#verbose = True		# global variable

############################################################################################################
############################################################################################################


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

#### Settings

mygpiopin = 23	# GPIO pin 23
logfile = './gpio-counter'

#### setup

GPIO.setmode(GPIO.BCM)
GPIO.setup(mygpiopin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

if len(sys.argv) > 1 and sys.argv[1] == 'debug':
	verbose = True
	print "Verbose is On"
	print "Logfile is " + logfile
	print "Current value is " + str(readvalue(logfile))
	print "GPIO is " + str(mygpiopin)
else:
	verbose = False

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



