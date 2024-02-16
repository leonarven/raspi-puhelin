import sys

import lib.audio as audio
import lib.const as const

from lib.logger import debug

from lib.GPIO import GPIO

def main():
	audio.playAudio( const.AUDIO_FILE_LAMMAS )

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		debug("Ohjelma lopetettu")
		GPIO.cleanup()
		sys.exit()
