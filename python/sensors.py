#!/usr/bin/env python
"""This is a program written to test and utilize the various sensors included in the CJRSLRB 16pcs/lots, 
and the KOOKYE 16 in 1 Smart Home Sensor Modules kits sold on Amazon.  

Each sensor interaction will be written as a class, and methods within that class will be documented.

Written by Joshua Simons 2020 joshua.a.simons@gmail.com

"""
progName = "sensors.py Version 0.1"

#Import Libraries we will be using
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import signal
import os

#GPIO pins.  Change the pin values to match your circuit----------------------------------------------

#GPIO pin to use to light LEDs
yellowPin = 17
greenPin = 27
redPin = 22

#LED Variables----------------------------------------------------------------------------------------
#Duration of each Blink
blinkDur = .1
#Number of times to Blink the LED
blinkTime = 7
#-----------------------------------------------------------------------------------------------------

#GPIO pin of button
buttonPin = 26

#GPIO pin of a Touch Sensor
touchPin = 

#Motion Sensor Pin
pirPin = 13

#Temp and Humidity Sensor (DHT11 or DHT22)
tempSensor = Adafruit_DHT.DHT22
#Temp and Humidity Sensor pin
tempPin = 19

#Ultra-Sonic Distance Measuring pins
trigPin = 24
echoPin = 25

#Sound Sensor pin
soundPin = 16



#Initialize the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(yellowPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pirPin, GPIO.IN)
GPIO.setup(trigPin,GPIO.OUT)
GPIO.setup(echoPin,GPIO.IN)
GPIO.setup(soundPin, GPIO.IN)

#------------------------------------------------------------------------------------------------------

#LED Control Class
class LED:
	def __init__(self, dur, time):
		self.dur = blinkDur
		self.Time = blinkTime

	def onOff(self, pin):
		GPIO.output(pin,True)
		time.sleep(blinkDur)
		GPIO.output(pin,False)
		time.sleep(blinkDur)

#------------------------------------------------------------------------------------------------------

# Use Class to create buttons
class Button:
	def __init__ (self, pin):
		self.pin = buttonPin

	def state(self):
		return GPIO.input(buttonPin)

	def clear(self):
		while True:
			input_state = GPIO.input(buttonPin)
			if input_state == False:
				os.system('clear')
			time.sleep(0.2)

#------------------------------------------------------------------------------------------------------


#Motion Detector Class (HC-SR501 infrared human body induction module)
class Motion:
	def __init__ (self, pin):
		self.pin = pirPin

	def state(self):
		return GPIO.input(pirPin)

#------------------------------------------------------------------------------------------------------
#Temperature and Humidity Sensor Class (Adafruit DHT11)
class Temperature:
	def __init__ (self, pin):
		self.pin = tempPin

	def readC(self):
		humidity, temperature = Adafruit_DHT.read_retry(tempSensor, tempPin)
		if humidity is not None and temperature is not None:
			tempCel = '{0:0.1f}*C'.format(temperature)
			return tempCel

	def readF(self):
		humidity, temperature = Adafruit_DHT.read_retry(tempSensor, tempPin)
                temperature = temperature * 9/5.0 +32
		if humidity is not None and temperature is not None:
                        tempFahr = '{0:0.1f}*F'.format(temperature)
			return tempFahr

	def readH(self):
		humidity, temperature = Adafruit_DHT.read_retry(tempSensor, tempPin)
		if humidity is not None and temperature is not None:
			humid = '{1:0.1f}%'.format(temperature, humidity)
			return humid

#------------------------------------------------------------------------------------------------------
#Ultra-Sonic Distance Measuring Class (HC-SR04)
class Ultrasonic:
	def __init__(self, trig, echo):
		self.trig = trigPin
		self.echo = echoPin

	def readDcm(self):
		#Let the sensor settle
		GPIO.output(trigPin, False)
		time.sleep(2)
		GPIO.output(trigPin, True)
		time.sleep(0.00001)
		GPIO.output(trigPin, False)
		#Take the readings

		while GPIO.input(echoPin) == 0:
			pulse_start = time.time()
		while GPIO.input(echoPin) == 1:
			pulse_end = time.time()

		pulse_duration = pulse_end - pulse_start
		distance = pulse_duration * 17150
		distance = round(distance,2)
		#Return Distance in CM
		return distance

        def readDin(self):
                #Let the sensor settle
                GPIO.output(trigPin, False)
                time.sleep(2)
                GPIO.output(trigPin, True)
                time.sleep(0.00001)
                GPIO.output(trigPin, False)
                #Take the readings
                while GPIO.input(echoPin) == 0:
                        pulse_start = time.time()
                while GPIO.input(echoPin) == 1:
                        pulse_end = time.time()
                pulse_duration = pulse_end - pulse_start
                distance = pulse_duration * 17150
                #Return Distance in Inches
		distance_in = distance / 2.54
		distance_in = round(distance_in,2)
		return distance_in

#Sound Sensor Trigger Class---------------------------------------------------------------------------
class SoundTrigger:
	def __init__(self, pin):
		self.pin = soundPin

	def trigger(self):
		while 1:
			if GPIO.input(soundPin) == GPIO.HIGH:
				i = 1 #number of iterations
				for l in range(1,i+1):
				#What to do when sound is triggered:
					os.system('clear')
					print "triggered"
				time.sleep(1)

#------------------------------------------------------------------------------------------------------
#Create Objects:=======================================================================================

#Create blinker as an LED object:
blinker = LED(blinkDur, blinkTime)
#Create switch as a Button object:
switch = Button(buttonPin)
#Create Motion Detector as an object
motion1 = Motion(pirPin)
#Create Temp and Humidity Object
weather = Temperature(tempPin)
dist = Ultrasonic(trigPin, echoPin)
soundsense = SoundTrigger(soundPin)

#------------------------------------------------------------------------------------------------------
#Do The Things!========================================================================================

#Clear the console and print "triggered" when sound is triggered--------------------------------------
#try:
#	soundsense.trigger()

#Print Distance Measurements from the sensor-----------------------------------------------------------
os.system('clear')
cm = str(dist.readDcm())
print(cm + " centimeters")
inch = str(dist.readDin())
print(inch + " inches")

#Print out the temp in Celcius and Fahrenheit----------------------------------------------------------
print weather.readC()
print weather.readF()
print weather.readH()

#Read Motion Detector State----------------------------------------------------------------------------
#try:
#	while True:
#		print motion1.state()
#		time.sleep(0.2)

#Read switch state-------------------------------------------------------------------------------------
#try:
#	while True:
#		if switch.state() == False:
#			print weather.readC()
#			print weather.readF()
#			print weather.readH()


#Make blinker blink
for i in range (blinkTime):
	blinker.onOff(yellowPin)
	blinker.onOff(greenPin)
	blinker.onOff(redPin)
	time.sleep(0.2)

#Use Clear function of the Button Class---------------------------------------------------------------
#try:
#	switch.clear()
#-----------------------------------------------------------------------------------------------------



#=====================================================================================================
#Cleanup  & Stuff--------------------------------------------------------------------------------------

#Use this when there is no loop to be broken:
os.system('clear')
print('gpio_control.py exited cleanly')
GPIO.cleanup()

#Use "Ctrl + c" to break the loop and then cleanup:
#except KeyboardInterrupt:
#	os.system('clear')
#	print('gpio_control.py exited cleanly')
#	GPIO.cleanup()
