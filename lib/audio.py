from pydub.generators import WhiteNoise, Sine

from pydub import AudioSegment
import pydub.playback

import sys
import time

from lib.logger import debug

import lib.const as const


def audioNameToAudioFile( name ):

	file = name;

	if name == const.AUDIO_FILE_LAMMAS:
		pass
	elif name == const.AUDIO_FILE_PM:
		pass
	elif name == const.AUDIO_FILE_PAD:
		pass

	elif name == const.AUDIO_PAD_1:
		file = const.AUDIO_FILE_PAD
	elif name == const.AUDIO_PAD_2:
		file = const.AUDIO_FILE_PAD
	elif name == const.AUDIO_PAD_3:
		file = const.AUDIO_FILE_PAD
	elif name == const.AUDIO_PAD_4:
		file = const.AUDIO_FILE_PAD
	elif name == const.AUDIO_PAD_5:
		file = const.AUDIO_FILE_PAD
	elif name == const.AUDIO_PAD_6:
		file = const.AUDIO_FILE_PAD
	elif name == const.AUDIO_PAD_7:
		file = const.AUDIO_FILE_PAD
	elif name == const.AUDIO_PAD_8:
		file = const.AUDIO_FILE_PAD
	elif name == const.AUDIO_PAD_9:
		file = const.AUDIO_FILE_PAD
	elif name == const.AUDIO_PAD_A:
		file = const.AUDIO_FILE_PAD
	elif name == const.AUDIO_PAD_0:
		file = const.AUDIO_FILE_PAD
	elif name == const.AUDIO_PAD_B:
		file = const.AUDIO_FILE_PAD
		
	else:
		return None

	return file;


AUDIO_FILES_CACHE = dict()

def generateAudio( name ):

	sound = None;

	file = audioNameToAudioFile( name );

	if file is not None:
		sound = AudioSegment.from_mp3( file )

	elif name == const.AUDIO_NOISE:
		noise = WhiteNoise()
		sound = noise.to_audio_segment( duration=1000,volume=0 )
		sound = sound - 20
		return sound
	
	else:
		return None;

	if file in AUDIO_FILES_CACHE:
		sound = AUDIO_FILES_CACHE[ file ]
	else:
		sound = AudioSegment.from_mp3( file )
		AUDIO_FILES_CACHE[ file ] = sound

	if name == const.AUDIO_PAD_1:
		sound = sound[const.AUDIO_PAD_SEQ_STARTS['1']:const.AUDIO_PAD_SEQ_ENDS['1']]
	elif name == const.AUDIO_PAD_2:
		sound = sound[const.AUDIO_PAD_SEQ_STARTS['2']:const.AUDIO_PAD_SEQ_ENDS['2']]
	elif name == const.AUDIO_PAD_3:
		sound = sound[const.AUDIO_PAD_SEQ_STARTS['3']:const.AUDIO_PAD_SEQ_ENDS['3']]
	elif name == const.AUDIO_PAD_4:
		sound = sound[const.AUDIO_PAD_SEQ_STARTS['4']:const.AUDIO_PAD_SEQ_ENDS['4']]
	elif name == const.AUDIO_PAD_5:
		sound = sound[const.AUDIO_PAD_SEQ_STARTS['5']:const.AUDIO_PAD_SEQ_ENDS['5']]
	elif name == const.AUDIO_PAD_6:
		sound = sound[const.AUDIO_PAD_SEQ_STARTS['6']:const.AUDIO_PAD_SEQ_ENDS['6']]
	elif name == const.AUDIO_PAD_7:
		sound = sound[const.AUDIO_PAD_SEQ_STARTS['7']:const.AUDIO_PAD_SEQ_ENDS['7']]
	elif name == const.AUDIO_PAD_8:
		sound = sound[const.AUDIO_PAD_SEQ_STARTS['8']:const.AUDIO_PAD_SEQ_ENDS['8']]
	elif name == const.AUDIO_PAD_9:
		sound = sound[const.AUDIO_PAD_SEQ_STARTS['9']:const.AUDIO_PAD_SEQ_ENDS['9']]
	elif name == const.AUDIO_PAD_A:
		sound = sound[const.AUDIO_PAD_SEQ_STARTS['A']:const.AUDIO_PAD_SEQ_ENDS['A']]
	elif name == const.AUDIO_PAD_0:
		sound = sound[const.AUDIO_PAD_SEQ_STARTS['0']:const.AUDIO_PAD_SEQ_ENDS['0']]
	elif name == const.AUDIO_PAD_B:
		sound = sound[const.AUDIO_PAD_SEQ_STARTS['B']:const.AUDIO_PAD_SEQ_ENDS['B']]

	return sound

# -------------------

AUDIO_SOUND_CACHE = dict()

def getOrGenerateAudio( name ):
	if not name in AUDIO_SOUND_CACHE:
		sound = generateAudio( name )
		AUDIO_SOUND_CACHE[ name ] = sound
	return AUDIO_SOUND_CACHE[ name ]

# -------------------

def playAudio( name ):
	sound = getOrGenerateAudio( name )
	debug( "audio.playAudio( name )", name )
	pydub.playback.play(sound)
	debug( "audio.playAudio( name )", name, "READY" )

def playSound( name, sound ):
	debug( "audio.playSound( name )", name )
	pydub.playback.play(sound)
	debug( "audio.playSound( name )", name, "READY" )

# -------------------

def playPadAudio( key ):
	audio_name = const.AUDIO_FILE_PAD + "#" + key
	playAudio( audio_name )

playPadAudioSequence = lambda sequence: [ playPadAudio( key ) for key in sequence ]

# -------------------

def initializeAudio( name ):
	debug( "audio.initializeAudio()", name )
	sound = getOrGenerateAudio( name )
	debug( "audio.initializeAudio()", name, "READY" )
	return sound

def init():
	initializeAudio( const.AUDIO_FILE_LAMMAS )
	initializeAudio( const.AUDIO_FILE_PM )
	initializeAudio( const.AUDIO_NOISE )
	debug( "audio.init() :: READY" )
	playAudio( const.AUDIO_NOISE )
