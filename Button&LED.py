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

# Configures GPIO Pin 18 as an input, because we want to
# "read" the state of the button. In this case we are affecting the state of the button and we want to the computer read its state.
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Going to an infinite loop. The loop will exit when we quit/escape our program.
while True:
	# In this case our logic is inverse due to our schematic. 
	# When the button is not pressed, the state is high.
	if(GPIO.input(18) == 1):
		print("Button State :OFF")
		# Since the button state is OFF, the LED is also OFF.
		GPIO.output(25, GPIO.LOW)
	
	# When the button is pressed, the state is low.
	if(GPIO.input(18) == 0):
		print("Button State :ON")
		#Since the button state is ON, the LED is also ON.
		GPIO.output(25, GPIO.HIGH)

# Resets all pins to factory settings upon exiting the program.
GPIO.cleanup()

