Readme File for Raspberry Pi Intro Class on July 21st, 2014


I. Necessary Parts

In order to proceed with these files, you must buy the following:

1. Resistors
2. LEDs
3. Breadboard
4. Wires
5. Push Button

I recommend that you buy these from Sparkfun. You will be able to buy everything in one place (see links below). Alternatively, you can buy everything  at RadioShack but expect to pay more.

II. Downloading these files

If you are looking at this page, make sure you are in the root directory of this folder. You should a "Download Zip" option to your right.
Click on that button and save it to your local hard drive. Next double click on the zip file and extract all the files. 


III. Circuit Diagram

I've created a Fritzing file for our schematic (program download link below). 
For those who don't know, Fritzing is a software that allows you to create schematics on your breadboard.
Follow the diagram and create your schematic exactly as shown. See PiIntro.fzz and/or PiIntro_schematic.pdf.

IV. Execution and editing

Open terminal up and navigate to the folder we extracted on Step II (see link below for navigating). 
You should see three python script files
	1. LED_on_off.py
	2. Button_state.py
	3. ButtonLED.py

To access/edit any of these files do the following without the brackets (see link below for using text editor nano):
	sudo nano {xxxxxxx.py}
	
To exit the file at any time from nano, press CTRL + X.

V. Run the Python scripts
Open the terminal up and navigate to the folder with our (3) python script files.

Type the following without brackets, followed by an enter:
	sudo python {xxxxxxxx.py}
	
To exit the file at any time, press CTRL + C.

VI. Links

Parts
Resistors -- https://www.sparkfun.com/products/10969
Leds -- https://www.sparkfun.com/products/9590
Breadboards -- https://www.sparkfun.com/products/9567 ; https://www.sparkfun.com/products/112
Jumper Wires (Male to Male) -- https://www.sparkfun.com/products/12795
Jumper Wires (Male to Female) -- https://www.sparkfun.com/products/12794
Push Button -- https://www.sparkfun.com/products/9190

Fritzing
http://fritzing.org/home/

Navigating on Terminal
http://www.penguintutor.com/raspberrypi/useful-command-reference

Using Nano as Text Editor
http://www.howtogeek.com/howto/42980/the-beginners-guide-to-nano-the-linux-command-line-text-editor/

