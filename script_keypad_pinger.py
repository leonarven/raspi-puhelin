
import sys

sys.path.append( './lib' )

from GPIO import GPIO
import const
import audio
import logger
import KeypadPinger
import KeypadHandler

# ----------------

pinger = KeypadPinger.KeypadPinger( const.KEYPAD_ROWS_PINS, const.KEYPAD_COLS_PINS )
keypad = KeypadHandler.KeypadHandler( pinger )

sound = audio.getOrGenerateAudio( const.AUDIO_FILE_PAD )

def detected( key ):

	print("[" , str( keypad.iteration ).zfill( 7 ) , "]", "Detected", key )

	if key in const.AUDIO_PAD_SEQ_STARTS:
		if key in const.AUDIO_PAD_SEQ_ENDS:
			audio.playSound( const.AUDIO_FILE_PAD+"#"+key, sound[ const.AUDIO_PAD_SEQ_STARTS[key]:const.AUDIO_PAD_SEQ_ENDS[key] ] )


keypad.registerKeydownListener( detected )


def main():
	while True:
		keypad.iterate();
		

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		logger.debug("Ohjelma lopetettu")
		GPIO.cleanup()
		sys.exit()
