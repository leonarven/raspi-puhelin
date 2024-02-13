
import sys
import time

sys.path.append( './lib' )

import audio

from logger import debug

import const
import Switch

from GPIO import GPIO

def onStateChangeActive( switch ):
	debug("Status vaihtunut -> Aktiivinen")
	audio.playAudio(const.AUDIO_FILE_LAMMAS)

def onStateChangeDisable( switch ):
	debug("Status vaihtunut -> Lepotila")
	audio.playAudio(const.AUDIO_FILE_PM)

switch = Switch.init()

def main():
	while True:
		switch.iterate( onStateChangeActive, onStateChangeDisable )

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		debug("Ohjelma lopetettu")
		GPIO.cleanup()
		sys.exit()
