import sys
import time

sys.path.append( '.' )

from lib.logger import debug
from lib.GPIO import GPIO

from lib.const import PIN_SWITCH_INPUT

class Switch:

	pin = None

	label = None

	state = 0

	def __init__( self, pin, label = None ):
		self.pin = pin

		if label is None:
			label = "pin_" + str( pin )

		self.label = label

		debug( "Switch.__init__( pin, label )", self.pin, self.label )

		GPIO.setup( self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

	def read(self):
		self.state = GPIO.input( self.pin )

		return self.state

	def isActive( self, read = True ):

		if read:
			self.read()

		return self.state == 1


	def getStateChange( self, debounce = 0.1 ):

			was_active = self.isActive( False )
			time.sleep( debounce );
			is_active  = self.isActive()

			if is_active:
					if not was_active:
							return 1
			else:
					if was_active:
							return 0

			return None

	def iterate( self, onStateChangeActive, onStateChangeDisable, debounce = 0.1 ):
			change = self.getStateChange( debounce );
			if change == 1:
				onStateChangeActive( self )
			elif change == 0:
				onStateChangeDisable( self )

def init( pin = PIN_SWITCH_INPUT ):
	switch = Switch( pin )
	return switch
