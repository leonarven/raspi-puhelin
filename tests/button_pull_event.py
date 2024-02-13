import sys
import time

sys.path.append( './lib' )

from logger import debug

import audio
import const
import Switch

from GPIO import GPIO

switch = Switch.init();

def onStateChangeActive( state ):
	print("onStateChangeActive", state)
	time.sleep( const.MS_100 )
	print( switch.read() )

def onStateChangeDisable( state ):
	print("onStateChangeDisable", state)

GPIO.add_event_detect( const.PIN_SWITCH_INPUT, GPIO.BOTH, callback=onStateChangeActive, bouncetime = 250 )
#GPIO.add_event_detect( const.PIN_SWITCH_INPUT, GPIO.FALLING, callback=onStateChangeDisable, bouncetime = 250 )

def main():
	asd = input("asd");

if __name__ == '__main__':
        try:
                main()
        except KeyboardInterrupt:
                debug("Ohjelma lopetettu")
                GPIO.cleanup()
                sys.exit()
