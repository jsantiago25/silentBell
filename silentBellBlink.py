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


while True:
	now = datetime.datetime.now()

	if (now.day == 4):
     		print(now.day)
		if (now.hour == 9 and now.minute > 25 and now.minute < 30):
			#print('It is: ' now.hour + now.minute) 
			wiringpi.digitalWrite(PIN_RED, red)
		        wiringpi.digitalWrite(PIN_GREEN, green)
      			wiringpi.digitalWrite(PIN_BLUE, blue)
        		print 'LedBorg on'
		else: 
			wiringpi.digitalWrite(PIN_RED, 0)
	                wiringpi.digitalWrite(PIN_GREEN, 0)
        	        wiringpi.digitalWrite(PIN_BLUE, 0)
               		print 'LedBorg off'

		

	else:
		if (now.hour == 8):
			if (now.minute < 35 and now.minute > 31):
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
		elif (now.hour == 9):
			if (now.minute < 20 and now.minute > 14):
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
		elif (now.hour == 10):
			if (now.minute < 5 and now.minute >= 0):
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
			elif (now.minute < 20 and > 14): 
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
                                print 'LedBorg off
		else:
			wiringpi.digitalWrite(PIN_RED, 0)
                        wiringpi.digitalWrite(PIN_GREEN, 0)
                        wiringpi.digitalWrite(PIN_BLUE, 0)

 

