#!/usr/bin/env python

import time
import wiringpi
wiringpi.wiringPiSetup()
 
# Setup the LedBorg GPIO pins
PIN_RED = 0
PIN_GREEN = 2
PIN_BLUE = 3
wiringpi.pinMode(PIN_RED, wiringpi.GPIO.OUTPUT)
wiringpi.pinMode(PIN_GREEN, wiringpi.GPIO.OUTPUT)
wiringpi.pinMode(PIN_BLUE, wiringpi.GPIO.OUTPUT)
 
# A function to set the LedBorg colours
def SetLedBorg(red, green, blue):
    wiringpi.digitalWrite(PIN_RED, red)
    wiringpi.digitalWrite(PIN_GREEN, green)
    wiringpi.digitalWrite(PIN_BLUE, blue)
 
# A function to turn the LedBorg off
def LedBorgOff():
    SetLedBorg(0, 0, 0)
 
# Settings for the sequence
colourSequence = [[1, 0, 0],    # Red
                  [0, 1, 0],    # Green
                  [0, 0, 1],    # Blue
                  [1, 1, 0],    # Yellow
                  [0, 1, 1],    # Cyan
                  [1, 0, 1],    # Magenta
                  [1, 1, 1]]    # White
delay = 2
 
# Set the LedBorg to each colour in turn
for colour in colourSequence:
    SetLedBorg(colour[0], colour[1], colour[2])
    print 'LedBorg colour:', colour
    time.sleep(delay)
 
# Turn the LedBorg off
LedBorgOff()
print 'LedBorg off'
