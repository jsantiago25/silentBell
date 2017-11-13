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
		#print(now.day) 
		#print(now.hour)
		#print(now.minute)
		if (now.hour == 11):
			if (now.minute < 29 and now.minute > 25):
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
		else:
			wiringpi.digitalWrite(PIN_RED, 0)
                        wiringpi.digitalWrite(PIN_GREEN, 0)
                        wiringpi.digitalWrite(PIN_BLUE, 0)

 
'''
	     # Wait for the time delay
     		time.sleep(delay)
 
		# Turn the LedBorg off
     		wiringpi.digitalWrite(PIN_RED, 0)
     		wiringpi.digitalWrite(PIN_GREEN, 0)
     		wiringpi.digitalWrite(PIN_BLUE, 0)
     		print 'LedBorg off'
		time.sleep(delay)

	else:
		wiringpi.digitalWrite(PIN_RED, 0)
                wiringpi.digitalWrite(PIN_GREEN, 0)
                wiringpi.digitalWrite(PIN_BLUE, 0)
		print 'Even minute'
		time.sleep(delay)  

while True:
     if ((now.minute % 2) == 0):  
     # Set the LedBorg colour
     	wiringpi.digitalWrite(PIN_RED, red)
     	wiringpi.digitalWrite(PIN_GREEN, green)
     	wiringpi.digitalWrite(PIN_BLUE, blue)
     	print 'LedBorg on'
 
     # Wait for the time delay
     	time.sleep(delay)
 
# Turn the LedBorg off
     	wiringpi.digitalWrite(PIN_RED, 0)
     	wiringpi.digitalWrite(PIN_GREEN, 0)
     	wiringpi.digitalWrite(PIN_BLUE, 0)
     	print 'LedBorg off'

'''


