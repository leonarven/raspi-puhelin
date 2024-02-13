import sys

sys.path.append( './lib' )

import audio
import const

def main():
	audio.playAudio( const.AUDIO_FILE_LAMMAS )

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		debug("Ohjelma lopetettu")
		GPIO.cleanup()
		sys.exit()
