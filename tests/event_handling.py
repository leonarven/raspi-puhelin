import sys

sys.path.append('.')

from lib.logger import debug

import lib.Operator as Operator
import lib.Feature  as Feature
import lib.Event    as Event



class HandsetMockReaderFeature( Feature.Feature ):

	def iterate( self ):
		
		self.iterations += 1

		if self.iterations % 20 == 0:
			self.events.emit( Event.HANDSET_STATUS_LIFTED, "Lifted" )

		if self.iterations % 20 == 10:
			self.events.emit( Event.HANDSET_STATUS_LOWERED, "Lowered" )



class KeypadMockReaderFeature( Feature.BaseKeypadFeature ):
	
	kc = 0
	
	def iterate( self ):
		
		self.iterations += 1

		if self.iterations % 10 == 0:
			self.kc += 1

			if self.kc >= len( self.keys ):
				self.kc = 0

			key = self.keys[ self.kc ]

			event = Event.KeypadPressedEvent( key )

			if event is not None:
				self.events.emit( event, "Pressed" )



class HandsetActionFeature( Feature.BaseHandsetActionFeature ):
	pass



class KeypadActionFeature( Feature.BaseKeypadActionFeature ):
	pass



def main():
	operator = Operator.Operator()

	operator.registerFeature( KeypadActionFeature( operator.events ) )
	operator.registerFeature( KeypadMockReaderFeature( operator.events ) )
	operator.registerFeature( HandsetMockReaderFeature( operator.events ) )
	operator.registerFeature( HandsetActionFeature( operator.events ) )

	while True:
		operator.iterate()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()
