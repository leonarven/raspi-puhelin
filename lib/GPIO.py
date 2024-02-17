from lib.MockGPIO import MockGPIO, FileMockGPIO

#import RPi.GPIO as GPIO

GPIO = FileMockGPIO()

GPIO.setwarnings( False )
GPIO.setmode( GPIO.BCM )