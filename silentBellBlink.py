#!/usr/bin/env python

#
import time
import datetime
import wiringpi
wiringpi.wiringPiSetup()
#
#
PIN_RED = 0
PIN_GREEN = 2
PIN_BLUE = 3
wiringpi.pinMode(PIN_RED, wiringpi.GPIO.OUTPUT) 
wiringpi.pinMode(PIN_GREEN, wiringpi.GPIO.OUTPUT)
wiringpi.pinMode(PIN_BLUE, wiringpi.GPIO.OUTPUT)  


red = 1
green = 1
blue = 0
delay = 1

def classFinishing():
	print 'Class finishing' 
        wiringpi.digitalWrite(PIN_RED, red)
        wiringpi.digitalWrite(PIN_GREEN, green)
        wiringpi.digitalWrite(PIN_BLUE, blue)
        print 'LedBorg on'
        time.sleep(delay)
        wiringpi.digitalWrite(PIN_RED, 0)
        wiringpi.digitalWrite(PIN_GREEN, 0)
        wiringpi.digitalWrite(PIN_BLUE, 0)
        time.sleep(delay)
        print 'LedBorg off'

while True:
	now = datetime.datetime.now()

	if (now.day == 4):
		if (now.hour == 8):
			if (now.minute <= 55 and now.minute > 50):
				classFinishing()  
		elif (now.hour == 9):  
			if (now.minute < 35 and now.minute > 29): 
				classFinishing() 
		elif (now.hour == 10):  
			if (now.minute < 15 and now.minute > 9): 
				classFinishing()  
			elif (now.minute < 30 and now.minute > 28): 
				classFinishing()  
		elif (now.hour == 11): 
			if (now.minute < 10 and now.minute > 4): 
				classFinishing() 
			elif (now.minute < 50 and now.minute > 44): 
				classFinishing() 
		elif (now.hour == 12):  
			if (now.minute < 40 and now.minute > 34): 
				classFinishing() 	
		elif (now.hour == 13): 
			if (now.minute < 30 and now.minute > 24):
				classFinishing()   
		elif (now.hour == 14): 
			if (now.minute < 20 and now.minute > 14):
				classFinishing() 
		elif (now.hour == 15):
			if (now.minute < 5 and now.minute >= 0):
				classFinishing()  
			elif (now.minute < 50 and now.minute >= 44):
				classFinshing() 
			elif (now.minute <= 49 an now.minute > 47):
				classFinishing()  
		else:
			wiringpi.digitalWrite(PIN_RED, 0)
                        wiringpi.digitalWrite(PIN_GREEN, 0)
                        wiringpi.digitalWrite(PIN_BLUE, 0)
		
	else:
		if (now.hour == 8):
			if (now.minute < 35 and now.minute > 33):
				classFinishing()   
		elif (now.hour == 9):
			if (now.minute < 20 and now.minute > 14):
				classFinishing()
		elif (now.hour == 10):
			if (now.minute < 5 and now.minute >= 0):
				classFinishing()
			elif (now.minute < 20 and > 14):
				classFinishing() 
		elif (now.hour == 11):
			if (now.minute < 5 and now.minute >= 0): 
				classFinishing()
			elif (now.minute < 50 and now.minute > 44):
				classFinishing() 
		elif (now.hour == 12): 
			if (now.minute < 40 and now.minute > 34): 
				classFinishing() 
		elif (now.hour == 13): 
			if (now.minute < 30 and now.minute > 24):
				classFinishing()   
		elif (now.hour == 14): 
			if (now.minute < 20 and now.minute > 14):
				classFinishing() 
		elif (now.hour == 15):
			if (now.minute < 5 and now.minute >= 0):
				classFinishing()  
			elif (now.minute < 50 and now.minute >= 44):
				classFinshing() 
			elif (now.minute <= 49 an now.minute > 47):
				classFinishing()  
		else:
			wiringpi.digitalWrite(PIN_RED, 0)
                        wiringpi.digitalWrite(PIN_GREEN, 0)
                        wiringpi.digitalWrite(PIN_BLUE, 0)

 

