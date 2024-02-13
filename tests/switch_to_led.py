# 
# Raspberry PI:lla ajettava ohjelma, joka osaa lukea kytkintä, lukea puhelimen näppäimistöä ja vilkuttaa valoa
# Ohjelman logiikka on seuraava:
# - Kun kytkin on normaalitilassa, se on kiinni ja ohjelma on lepotilassa.
# - Kun kytkin on auki, ohjelma on aktiivinen.
# - Kun ohjelma on aktiivinen, niin se odottaa puhelimen näppäimistöltä merkkijonoa, joka on muotoa "1,2,3,4,5,6,7,8,9,0".
# - Kun ohjelma on aktiivinen ja se saa oikean merkkijonon, niin se vilkuttaa valoa 5 kertaa.
# - Kun ohjelma on aktiivinen ja se saa väärän merkkijonon, niin se vilkuttaa valoa 2 kertaa.
#
# Ohjelma sisältää seuraavat metodit:
# - read_switch(): lukee kytkintä
# - read_keyboard(): lukee puhelimen näppäimistöä
# - blink(): vilkuttaa valoa
# - main(): ohjelman päämetodi

import audio

from logger import debug

import const
from switch import Switch

from GPIO import GPIO

import time
import sys
import os

# GPIO:n pinnien numerointi
GPIO.setwarnings( False )
GPIO.setmode( GPIO.BCM )

# GPIO:n pinnien tilat
GPIO.setup( const.PIN_STATUS_LED, GPIO.OUT ) # valo

GPIO.setup( const.PIN_KEYBOARD_1, GPIO.IN ) # valo
#GPIO.setup( const.PIN_KEYBOARD_2, GPIO.IN ) # valo
GPIO.setup( const.PIN_KEYBOARD_3, GPIO.IN ) # valo
GPIO.setup( const.PIN_KEYBOARD_4, GPIO.IN ) # valo
GPIO.setup( const.PIN_KEYBOARD_5, GPIO.IN ) # valo
GPIO.setup( const.PIN_KEYBOARD_6, GPIO.IN ) # valo
GPIO.setup( const.PIN_KEYBOARD_7, GPIO.IN ) # valo
GPIO.setup( const.PIN_KEYBOARD_8, GPIO.IN ) # valo
GPIO.setup( const.PIN_KEYBOARD_9, GPIO.IN ) # valo

switch = Switch( const.PIN_SWITCH_INPUT )

# Valon tila
light_state = 0

# Puhelimen näppäimistön lukeminen
def read_keyboard():
	keyboard_input = input("Anna koodi: ")
	return keyboard_input

# Valon vilkuttaminen
def blink( count ):
	global light_state
	for i in range(0, count):
		GPIO.output( const.PIN_STATUS_LED, GPIO.HIGH )
		time.sleep(0.2)
		GPIO.output( const.PIN_STATUS_LED, GPIO.LOW )
		time.sleep(0.2)
	light_state = 0

# Ohjelman päämetodi
def main():
	global switch_state
	global light_state

	while True:

		was_active = switch.isActive( False )
		time.sleep(1)
		is_active  = switch.isActive()

		if is_active:
			if not was_active:
				debug("Status vaihtunut -> Aktiivinen")

			else:

				keyboard_input = read_keyboard()

				if keyboard_input == "1,2,3,4,5,6,7,8,9,0":
					blink( 5 )
				else:
					blink( 2 )

		else:
			if was_active:
				debug("Status vaihtunut -> Lepotila")

				GPIO.output( const.PIN_STATUS_LED, GPIO.LOW )

			else:

				time.sleep(1)

# Ohjelman suoritus
try:
	main()
except KeyboardInterrupt:
	debug("Ohjelma lopetettu")
	GPIO.cleanup()
	sys.exit()

