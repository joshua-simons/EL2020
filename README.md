# EL2020

### mq2 Branch

Ok, this is a quick and dirty example of how to use the mq2 smoke sensor to detect smoke.  I am using the sensor with the digital output (DO) because if you are using multiple sensors you want to save the one analog/digital converter in the kit for something more important.

I guess the best general advice I can give you is to look up the sensor, and figure out what it's expected behavior is, and then figure out how you want to use it.  This particular sensor has both a digital and an analog output.  THe digital output basically triggers in the same way a motion detector sensor or a sound sensor triggers.  You set the threshold on the sensor, and once that threshold is exceeded, the sensor sends voltage via a pin (or in some cases grounds that pin).

In this example I am using GPIO pin 17 for the smoke sensor, and 3.3v for the vcc.  This should give you an idea of how to use this type of sensor.  Note: You do not need to install any libraries to use this one.  You just need the RPi.GPIO and time libraries.  I added the sys library for a clean exit, but you do you.

The mq2.py code is in the python folder.

Here's a video of it working with additional commentary:

https://photos.app.goo.gl/uvDpauH5FPteYPfH8
