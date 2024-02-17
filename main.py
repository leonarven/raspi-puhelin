import sys

from lib.GPIO   import GPIO
from lib.logger import debug

import lib.const         as const
import lib.audio         as audio
import lib.Switch        as Switch
import lib.Operator      as Operator
import lib.Feature       as Feature
import lib.KeypadPinger  as KeypadPinger
import lib.KeypadHandler as KeypadHandler



class HandsetActionFeature( Feature.BaseHandsetActionFeature ):

	def __init__( self, events ):
		super().__init__( events )

		audio.initializeAudio( const.AUDIO_FILE_PM )
		audio.initializeAudio( const.AUDIO_FILE_LAMMAS )

	def onHandsetStatusLowered( self, data ):
		audio.playAudio( const.AUDIO_FILE_PM )

	def onHandsetStatusLifted( self, data ):
		audio.playAudio( const.AUDIO_FILE_LAMMAS )



class KeypadActionFeature( Feature.BaseKeypadActionFeature ):

	def __init__( self, events ):
		super().__init__( events )

		self.sound = audio.initializeAudio( const.AUDIO_FILE_PAD )

	def onKeypadKeydown( self, key, data ):
		super().onKeypadKeydown( key, data )

		if key in const.AUDIO_PAD_SEQ_STARTS:
			if key in const.AUDIO_PAD_SEQ_ENDS:
				audio.playSound( const.AUDIO_FILE_PAD+"#"+key, self.sound[ const.AUDIO_PAD_SEQ_STARTS[key]:const.AUDIO_PAD_SEQ_ENDS[key] ] )



class KeypadInputActionFeature( Feature.BaseKeypadInputActionFeature ):
	def onKeypadInput( self, data ):
		audio.playPadAudioSequence( data )



import lib.Event as Event

def main():
	operator = Operator.Operator()

	pinger = KeypadPinger.KeypadPinger( const.KEYPAD_ROWS_PINS, const.KEYPAD_COLS_PINS )
	keypad = KeypadHandler.KeypadHandler( pinger )

	operator.registerFeature( Feature.HandsetReaderFeature( operator.events, Switch.init() ) )
	operator.registerFeature( Feature.KeypadReaderFeature(  operator.events, keypad ) )
	operator.registerFeature( Feature.KeypadEndkeyInputFeature( operator.events, const.KEYPAD_KEY_HASH ) )

	operator.registerFeature( HandsetActionFeature( operator.events ) )
	operator.registerFeature( KeypadActionFeature(  operator.events ) )
	operator.registerFeature( KeypadInputActionFeature( operator.events ) )

	while True:
		operator.iterate()



if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()
