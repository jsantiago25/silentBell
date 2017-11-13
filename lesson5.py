#!/usr/bin/env python
 
# Import library functions we need
import time
import wiringpi
wiringpi.wiringPiSetup()
 
# Setup software PWMs on the GPIO pins
PIN_RED = 0
PIN_GREEN = 2
PIN_BLUE = 3
LED_MAX = 100
wiringpi.softPwmCreate(PIN_RED,   0, LED_MAX)
wiringpi.softPwmCreate(PIN_GREEN, 0, LED_MAX)
wiringpi.softPwmCreate(PIN_BLUE,  0, LED_MAX)
wiringpi.softPwmWrite(PIN_RED,   0)
wiringpi.softPwmWrite(PIN_GREEN, 0)
wiringpi.softPwmWrite(PIN_BLUE,  0)
 
# A function to set the LedBorg colours
def SetLedBorg(red, green, blue):
    wiringpi.softPwmWrite(PIN_RED,   int(red   * LED_MAX))
    wiringpi.softPwmWrite(PIN_GREEN, int(green * LED_MAX))
    wiringpi.softPwmWrite(PIN_BLUE,  int(blue  * LED_MAX))
 
# A function to turn the LedBorg off
def LedBorgOff():
    SetLedBorg(0, 0, 0)
 
# Run until the user presses CTRL+C
print 'Press CTRL+C to exit'
while True:
    # Loop over a set of different hues:
    for hue in range(300):
        # Get hue into the 0 to 3 range
        hue /= 100.0
        # Decide which two channels we are between
        if hue < 1.0:
            # Red to Green
            red = 1.0 - hue
            green = hue
            blue = 0.0
        elif hue < 2.0:
            # Green to Blue
            red = 0.0
            green = 2.0 - hue
            blue = hue - 1.0
        else:
            # Blue to Red
            red = hue - 2.0
            green = 0.0
            blue = 3.0 - hue
        # Set the chosen colour
        SetLedBorg(red, green, blue)
        # Wait a short while
        time.sleep(0.1)

