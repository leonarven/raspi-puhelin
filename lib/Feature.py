
from logger import debug

import Event



class Feature:

	iterations = 0

	def __init__( self, events ):
		self.events = events;

	def iterate( self ):
		pass



class BaseKeypadFeature( Feature ):

	keys = [ "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "0", "B", "R" ]
	key_events = dict()

	def __init__(self, events):
		super().__init__(events)

		for key in self.keys: self.key_events[ key ] = Event.KeypadPressedEvent( key )



class BaseKeypadActionFeature( BaseKeypadFeature ):

	def __init__( self, events ):
		super().__init__( events )
		
		for key in self.key_events:
			self.injectEventListener( key, self.key_events[key] )

	def injectEventListener( self, key, event ):

		if event is not None:

			self.events.on( event, lambda data: self.onKeypadKeydown( key, data ) )

	def onKeypadKeydown( self, key, data = None ):
		debug( "BaseKeypadActionFeature.onKeypadKeydown()", key, data )



class BaseHeadsetActionFeature( Feature ):
	def __init__( self, events ):
		super().__init__( events )

		events.on( Event.HANDSET_STATUS_LIFTED, self.onHandsetStatusLifted )
		events.on( Event.HANDSET_STATUS_LOWERED, self.onHandsetStatusLowered )

	def onHandsetStatusLifted( self, data ):
		debug( "BaseHeadsetActionFeature.onHandsetStatusLifted()", data )

	def onHandsetStatusLowered( self, data ):
		debug( "BaseHeadsetActionFeature.onHandsetStatusLowered()", data )