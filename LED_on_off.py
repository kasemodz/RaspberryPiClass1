# The purpose of this code is to turn the led off and on.
# The LED is connected to GPIO pin 25 via a 220 ohm resistor.
# See Readme file for necessary components 

#! /usr/bin/python
#We are importing the sleep from the time module.
from time import sleep

#We are importing GPIO subclass from the class RPi. We are referring to this subclass via GPIO.
import RPi.GPIO as GPIO

# Resets all pins to factory settings
GPIO.cleanup() 

# Sets the mode to pins referred by "GPIO__" pins (i.e. GPIO24)
GPIO.setmode(GPIO.BCM)

# Configures GPIO Pin 25 as an output, because we want to
# control the state of the LED with this code.
GPIO.setup(25, GPIO.OUT)

# Turns the LED state to ON by the HIGH command. To turn off the LED, change HIGH to LOW, 
# then run this file again. ie. GPIO.output(25, GPIO.LOW)
GPIO.output(25, GPIO.HIGH)


