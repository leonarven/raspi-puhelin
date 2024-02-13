import sys

sys.path.append( './lib' )

from logger import debug

import Operator
import Feature
import Event



class HeadsetMockReaderFeature( Feature.Feature ):

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



class HeadsetActionFeature( Feature.BaseHeadsetActionFeature ):
	pass



class KeypadActionFeature( Feature.BaseKeypadActionFeature ):
	pass



def main():
	operator = Operator.Operator()

	operator.registerFeature( KeypadActionFeature( operator.events ) )
	operator.registerFeature( KeypadMockReaderFeature( operator.events ) )
	operator.registerFeature( HeadsetMockReaderFeature( operator.events ) )
	operator.registerFeature( HeadsetActionFeature( operator.events ) )

	while True:
		operator.iterate()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()
