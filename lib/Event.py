
HANDSET_STATUS_LIFTED = "HANDSET_LIFTED"
HANDSET_STATUS_LOWERED = "HANDSET_LOWERED"

_PRESSED_KEYPAD__PREFIX = "PRESSED_KEYPAD_";

PRESSED_KEYPAD_1 = _PRESSED_KEYPAD__PREFIX + "1"
PRESSED_KEYPAD_2 = _PRESSED_KEYPAD__PREFIX + "2"
PRESSED_KEYPAD_3 = _PRESSED_KEYPAD__PREFIX + "3"
PRESSED_KEYPAD_4 = _PRESSED_KEYPAD__PREFIX + "4"
PRESSED_KEYPAD_5 = _PRESSED_KEYPAD__PREFIX + "5"
PRESSED_KEYPAD_6 = _PRESSED_KEYPAD__PREFIX + "6"
PRESSED_KEYPAD_7 = _PRESSED_KEYPAD__PREFIX + "7"
PRESSED_KEYPAD_8 = _PRESSED_KEYPAD__PREFIX + "8"
PRESSED_KEYPAD_9 = _PRESSED_KEYPAD__PREFIX + "9"
PRESSED_KEYPAD_A = _PRESSED_KEYPAD__PREFIX + "A"
PRESSED_KEYPAD_0 = _PRESSED_KEYPAD__PREFIX + "0"
PRESSED_KEYPAD_B = _PRESSED_KEYPAD__PREFIX + "B"

PRESSED_R = "PRESSED_R"



def KeypadPressedEvent( key ):

	name = None

	if key == "R":
		name = PRESSED_R
	else:
		name = _PRESSED_KEYPAD__PREFIX + key;

	return name



class Handler:
	
	# A list of events and their listeners
	events = {}

	# Register an event and its listener
	def on( self, event, listener ):

		if event not in self.events:
			self.events[event] = []

		self.events[event].append(listener)

	# Raise an event
	def emit( self, event, data ):

		if event in self.events:
			for listener in self.events[event]:
				listener(data)