import sys
import time

sys.path.append('.')

from lib.logger import debug
from lib.GPIO   import GPIO

import lib.const  as const
import lib.Switch as Switch


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
