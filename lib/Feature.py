
from logger import debug
from GPIO import GPIO

import Event
import time




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



class KeypadReaderFeature( BaseKeypadFeature ):

    def __init__( self, events, keypad ):
        super().__init__( events )

        self.keypad = keypad

        self.keypad.registerKeydownListener( self.onKeydown )

    def iterate( self ):
        self.keypad.iterate();

    def onKeydown( self, key ):
        if key in self.key_events:
            self.events.emit( self.key_events[key], key )



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



class BaseHandsetActionFeature( Feature ):
	def __init__( self, events ):
		super().__init__( events )

		events.on( Event.HANDSET_STATUS_LIFTED, self.onHandsetStatusLifted )
		events.on( Event.HANDSET_STATUS_LOWERED, self.onHandsetStatusLowered )

	def onHandsetStatusLifted( self, data ):
		debug( "BaseHandsetActionFeature.onHandsetStatusLifted()", data )

	def onHandsetStatusLowered( self, data ):
		debug( "BaseHandsetActionFeature.onHandsetStatusLowered()", data )



class HandsetReaderFeature( Feature ):

    def __init__( self, events, switch ):
        super().__init__(events)

        self.switch = switch

        GPIO.add_event_detect( self.switch.pin, GPIO.BOTH, callback=self.onStateChangeActive, bouncetime=250 )

    def onStateChangeActive( self, state ):

        time.sleep( 0.100 )

        if self.switch.read() == GPIO.HIGH:
            self.events.emit( Event.HANDSET_STATUS_LIFTED, "Lifted" )
        else:
            self.events.emit( Event.HANDSET_STATUS_LOWERED, "Lowered" )
