
import sys

sys.path.append( './lib' )

from GPIO import GPIO
import const
import audio
import logger
import KeypadPinger
import KeypadHandler

# ----------------

PIN_C1 = const.PIN_KEYBOARD_3
PIN_C2 = const.PIN_KEYBOARD_4
PIN_C3 = const.PIN_KEYBOARD_6

PIN_R1 = const.PIN_KEYBOARD_9
PIN_R2 = const.PIN_KEYBOARD_8
PIN_R3 = const.PIN_KEYBOARD_7
PIN_R4 = const.PIN_KEYBOARD_5

# ----------------

pinger = KeypadPinger.KeypadPinger([ PIN_R1, PIN_R2, PIN_R3, PIN_R4 ], [ PIN_C1, PIN_C2, PIN_C3 ]);
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
