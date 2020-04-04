#!/usr/bin/python

# Import libraries
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from random import randint, choice
from time import sleep
from datetime import datetime

sense = SenseHat()
sense.clear()
sense.gamma_reset()

# Some colours, in the format R,G,B -> 0-255 per colour
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
purple = (128, 0, 128)
black = (0, 0, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)


# The default colour to flash LEDs
defaultColour = blue

# Random colour 
def randomColour():
	return (randint(0, 255), randint(0, 255), randint(0, 255))

# Pressure in millibar
def pressure():
	press = sense.get_pressure()
	pressureFormatted = "Pressure:{0}".format(press)
	return pressureFormatted

def temp():
	temp = sense.get_temperature()
	tempFormatted = "Temp:{0:.2f}".format(temp) + "'C"
	if temp in range(0, 17):
		tempColour = blue
	elif temp in range(0, 23):
		tempColour = green
	else:
		tempColour = red
	return tempFormatted, tempColour


def humidity():
	hum = sense.get_humidity()
	humidtyFormatted = "Humidity:{0:.2f}".format(hum)
	return humidtyFormatted


def clock():
	now = datetime.now()
	return now.strftime("%H:%M")


def date():
	now = datetime.now()
	return now.strftime("%d:%m:%Y")


# Loads an image to display on the LEDs
def spaceInvader():
	sense.load_image('space_invader.png')


if __name__ == "__main__":
	spaceInvader()
	sleep(2)
	sense.clear()
	while True:
		event = sense.stick.wait_for_event()
		if(event.action == ACTION_PRESSED):
			if(event.direction == "right"):
				sense.show_message(date(), text_colour=randomColour())
			elif(event.direction == "left"):
				sense.show_message(clock(), text_colour=randomColour())
			elif(event.direction == "up"):
				temperature, colour = temp()
				sense.show_message(temperature, text_colour=colour)
			elif(event.direction == "down"):
				sense.show_message(humidity(), text_colour=randomColour())
			elif(event.direction == "middle"):
				sense.show_message(pressure(), text_colour=randomColour())
