
from logger import debug
import const

def pinToString( pin ):
    if pin in const.reverseTable:
        return f'{ const.reverseTable[pin] }={ pin }'
    else:
        return str( pin );

class MockGPIO:

    BCM      = "BCM"
    IN       = "IN"
    OUT      = "OUT"
    HIGH     = "HIGH"
    LOW      = "LOW"
    PUD_DOWN = "PUD_DOWN"
    RISING   = "RISING"
    FALLING  = "FALLING"


    def add_event_detect( self, pin, mode, **kwargs ):
        debug("MockGPIO.add_event_detect(", pin, ",", mode, ",", kwargs, ")")

    def setmode(self, mode):
        debug("MockGPIO.setmode(", mode, ")")

    def setwarnings(self, mode):
        debug("MockGPIO.setwarnings(", mode, ")")

    def setup(self, pin, mode, **kwargs):
        debug("MockGPIO.setup(", pinToString(pin), ",", mode, ")")

    def input(self, pin):
        debug("MockGPIO.input(", pinToString(pin), ")")
        return 0

    def output(self, pin, mode):
        debug("MockGPIO.output(", pinToString(pin), ",", mode, ")")

    def cleanup(self):
        debug("MockGPIO.cleanup()")

    def __init__(self):
        debug("MockGPIO.__init__()")


#import RPi.GPIO as GPIO
#GPIO =  GPIO

GPIO = MockGPIO()

GPIO.setwarnings( False )
GPIO.setmode( GPIO.BCM )

