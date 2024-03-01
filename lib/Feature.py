import time

from lib.logger import debug
from lib.GPIO import GPIO

import lib.Event as Event

import lib.const as const




class Feature:

	iterations = 0

	def __init__( self, events ):
		self.events = events;

	def iterate( self ):
		pass



class BaseKeypadFeature( Feature ):

	keys = const.KEYPAD_KEYS
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
		

		events.on( Event.KEYPAD_SEQUENCE, self.onKeypadSequence )
		events.on( Event.KEYPAD_INPUT,    self.onKeypadInput )
		events.on( Event.KEYPAD_CLEAR,    self.onKeypadClear )

	def injectEventListener( self, key, event ):

		if event is not None:
			self.events.on( event, lambda data: self.onKeypadKeydown( key, data ) )


	def onKeypadKeydown( self, argv1 = None, argv2 = None, argv3 = None ):
		debug( type(self).__name__,".onKeypadKeydown()",  argv1, argv2, argv3 )

	def onKeypadSequence( self, argv1 = None, argv2 = None, argv3 = None ):
		debug( type(self).__name__,".onKeypadSequence()", argv1, argv2, argv3 )

	def onKeypadInput( self, argv1 = None, argv2 = None, argv3 = None ):
		debug( type(self).__name__,".onKeypadInput()",     argv1, argv2, argv3 )

	def onKeypadClear( self, argv1 = None, argv2 = None, argv3 = None ):
		debug( type(self).__name__,".onKeypadClear()",     argv1, argv2, argv3 )



class BaseKeypadSequenceActionFeature( BaseKeypadActionFeature ):

	pad_stack = []

	def onKeypadKeydown( self, key, data = None ):
		self.pad_stack.append( key )

		self.events.emit( Event.KEYPAD_SEQUENCE, self.pad_stack )

	def onKeypadClear( self, data ):
		self.pad_stack = [];


""" class BaseKeypadInputActionFeature( BaseKeypadActionFeature ):
	
	def __init__( self, events ):
		super().__init__( events )
		events.on( Event.KEYPAD_INPUT, self.onKeypadInput )

	def onKeypadInput( self, data ):
		debug( "BaseKeypadInputActionFeature.onKeypadInput()", data ) """


class KeypadEndkeyInputFeature( BaseKeypadActionFeature ):

	def __init__( self, events, endkey = const.KEYPAD_KEY_HASH ):
		super().__init__( events )

		self.endkey = endkey


	def onKeypadSequence( self, seq ):
		key = seq.pop()

		if key == self.endkey:
			self.events.emit( Event.KEYPAD_CLEAR )
			self.events.emit( Event.KEYPAD_INPUT, seq )


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
