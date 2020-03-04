import RPi.GPIO as GPIO
import time
import os

#Initialize the GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)
GPIO.setup(17, GPIO.OUT)

def blinkOnce(pin):
	GPIO.output(pin,True)
	time.sleep(1)
	GPIO.output(pin,False)
	time.sleep(1)


touchstatus = False
#read digital touch sensor
def read_touchsensor():
	global touchstatus
	if(GPIO.input(26)==True):
		touchstatus = not touchstatus
		if touchstatus:
			blinkOnce(17)
		else:
			GPIO.output(17,False)
	pass

try:
	while True:
		read_touchsensor()


except KeyboardInterrupt:
	GPIO.cleanup()

