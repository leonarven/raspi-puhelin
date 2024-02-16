
from lib.logger import debug
from lib.GPIO import GPIO, MockGPIO

import lib.Event as Event

class Operator:

	events = Event.Handler();

	features = []

	def __init__( self ):
		pass


	def registerFeature( self, feature ):
		self.features.append( feature )


	def iterate( self ):

		if isinstance( GPIO, MockGPIO ):
			GPIO.iterate()

		#debug( "Operator.iterate()" )

		for feature in self.features:
			feature.iterate()
