import time

import lib.const  as const
import lib.Switch as Switch

from lib.GPIO import GPIO


class KeypadPinger: 

	delay_counter = 0

	row_pins = [ None, None, None, None ]
	col_pins = [ None, None, None ]

	cols_state = [ GPIO.LOW, GPIO.LOW, GPIO.LOW ]

	def __init__( self, row_pins, col_pins ):
		self.row_pins = row_pins
		self.col_pins = col_pins

		[ GPIO.setup(  pin, GPIO.OUT ) for pin in col_pins ]
		[ GPIO.output( pin, GPIO.LOW ) for pin in col_pins ]

		self.switchs = [
			Switch.Switch( row_pins[3], "pin_" + str(const.PIN_KEYBOARD_5) + " / pad_5 / R4" ),
			Switch.Switch( row_pins[2], "pin_" + str(const.PIN_KEYBOARD_7) + " / pad_7 / R3" ),
			Switch.Switch( row_pins[1], "pin_" + str(const.PIN_KEYBOARD_8) + " / pad_8 / R2" ),
			Switch.Switch( row_pins[0], "pin_" + str(const.PIN_KEYBOARD_9) + " / pad_9 / R1" )
		]

	
	def __delay( self ):
		self.delay_counter += 1
		#print("[" , str(self.delay_counter).zfill(7) , "]")
		time.sleep( const.MS_10*5 )

	def __apply( self ):
		GPIO.output( self.col_pins[0], self.cols_state[0] )
		GPIO.output( self.col_pins[1], self.cols_state[1] )
		GPIO.output( self.col_pins[2], self.cols_state[2] )

	def __clear( self ):
		self.cols_state = [ GPIO.LOW, GPIO.LOW, GPIO.LOW ]

	def clear( self ):
		self.__clear()
		self.__apply()
		self.__delay()

	def apply( self ):

		self.__clear()

		if self.active_col is not None:
			self.cols_state[ self.active_col ] = GPIO.HIGH

		self.__apply()
		self.__delay()

	def activateCol( self, col ):
		self.active_col = col;
		self.apply()


	def readCol( self ):
		return [
			GPIO.input( self.row_pins[0] ),
			GPIO.input( self.row_pins[1] ),
			GPIO.input( self.row_pins[2] ),
			GPIO.input( self.row_pins[3] )
		]
	
	def readActiveRows( self ):
		return [ i for i, v in enumerate( self.readCol() ) if v == GPIO.HIGH ]
	
	def iterateActiveKey( self ):

		self.activateCol( 0 )
		r1 = self.readActiveRows()
		self.activateCol( 1 )
		r2 = self.readActiveRows()
		self.activateCol( 2 )
		r3 = self.readActiveRows()

		return [ r1, r2, r3 ]