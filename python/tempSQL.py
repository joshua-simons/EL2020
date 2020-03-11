#Import Libraries
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import os
import sqlite3 as sql
import smtplib


#Globals
redPin = 27
greenPin = 22
tempPin = 17
buttonPin = 26

tempSensor = Adafruit_DHT.DHT22

#Temp and Humidity Sensor
tempSensor = Adafruit_DHT.DHT22
#LED Variables---------------------------------------------------------------------------------------
#Duration of each Blink
blinkDur = .1
#Number of times to Blink the LED
blinkTime = 7
#----------------------------------------------------------------------------------------------------

#SMTP eMail Variables
eFROM = "kd2egt@gmail.com"
eTO = "8453094409@msg.fi.google.com"
Subject = "Alert!"
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

#Connect to the database
con = sqlite.connect('../log/tempLog.db')
cur = con.cursor()

#Set the initial checkbit to 0.  This will throw a warning when run, but will still work just fine
eChk = 0

#Initialize the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def oneBlink(pin):
	GPIO.output(pin,True)
	time.sleep(blinkDur)
	GPIO.output(pin,False)
	time.sleep(blinkDur)

def alert(tempF):
	global eChk
	if eChk == 0:
		Text = "The monitor now indicates that the temperature is now "+str(tempF)
		eMessage = 'Subject: {}\n\n{}'.format(Subject, Text)
		server.login("kd2egt@gmail.com", "ybihbernfcvynzju")
		server.sendmail(eFROM, eTO, eMessage)
		server.quit
		eChk = 1

def readDHT(tempPin):
	humidity, temperature = Adafruit_DHT.read_retry(tempSensor, tempPin)
	temperature = temperature * 9/5.0 +32
	if humidity is not None and temperature is not None:
		tempF = '{0:0.1f}'.format(temperature)
		humid = '{1:0.1f}'.format(temperature, humidity)
	else:
		print('Error Reading Sensor')

	return tempF, humid

#Dummy time for first itteration of the loop
oldTime = 60

#Read Temperature right off the bat
tempF, hum = readDHT(tempPin)

try:
	while True:
	#Send text message alert if temperature is out of range
		if 68 <= float(tempF) <= 78:
			eChk = 0
		else:
			alert(tempF)
		#if loop set for every 60 seconds
		if time.time() - oldTime > 59:
			tempF, hum = readDHT()
			if not data:
				time.sleep(5)
				continue
			#Defines and executes the sql query (templog is the table name in the .db)
			query = "INSERT INTO templog (Date, Temperature, Humidity) VALUES ('{}', '{}', '{}');"
			query = query.format(time.strftime("%Y-%m-%d %H:%M:%S"), tempF, humid)
			cur.execute(query)
			con.commit()
			print(time.strftime("%Y-%m-%d %H:%M:%S")+" "+tempF+"*F "+humid+"%")
			oldTime = time.time()

except KeyboardInterrupt:
	os.system('clear')
	con.close()
	print ("Temperature Logger and Web App Exited Cleanly")
	exit(0)
	GPIO.cleanup