
import sys
import time

sys.path.append( '.' )

import lib.audio as audio

from lib.logger import debug

import lib.const as const
import lib.Switch as Switch

from lib.GPIO import GPIO

def onStateChangeActive( switch ):
	debug("Status vaihtunut -> Aktiivinen")
	audio.playAudio(const.AUDIO_FILE_LAMMAS)

def onStateChangeDisable( switch ):
	debug("Status vaihtunut -> Lepotila")
	audio.playAudio(const.AUDIO_FILE_PM)

switch = Switch.init()

def main():
	while True:
		GPIO.iterate();
		switch.iterate( onStateChangeActive, onStateChangeDisable )

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		debug("Ohjelma lopetettu")
		GPIO.cleanup()
		sys.exit()
