
DEBUG = True

DO_FAKE_SST = not True
DO_FAKE_LLM = not True
DO_FAKE_TTS = not True

# -----------------

MS_1000 = 1
MS_100  = 0.1
MS_10   = 0.01

AUDIO_NOISE        = "__whitenoise__"
AUDIO_FILE_LAMMAS  = "assets/lammas.mp3"
AUDIO_FILE_PM      = "assets/pm.mp3"
AUDIO_FILE_PAD     = "assets/pad.mp3"
AUDIO_PAD_1        = "assets/pad.mp3#1"
AUDIO_PAD_2        = "assets/pad.mp3#2"
AUDIO_PAD_3        = "assets/pad.mp3#3"
AUDIO_PAD_4        = "assets/pad.mp3#4"
AUDIO_PAD_5        = "assets/pad.mp3#5"
AUDIO_PAD_6        = "assets/pad.mp3#6"
AUDIO_PAD_7        = "assets/pad.mp3#7"
AUDIO_PAD_8        = "assets/pad.mp3#8"
AUDIO_PAD_9        = "assets/pad.mp3#9"
AUDIO_PAD_A        = "assets/pad.mp3#A"
AUDIO_PAD_0        = "assets/pad.mp3#0"
AUDIO_PAD_B        = "assets/pad.mp3#B"

# -----------------

KEYPAD_KEY_1 = "1"
KEYPAD_KEY_2 = "2"
KEYPAD_KEY_3 = "3"
KEYPAD_KEY_4 = "4"
KEYPAD_KEY_5 = "5"
KEYPAD_KEY_6 = "6"
KEYPAD_KEY_7 = "7"
KEYPAD_KEY_8 = "8"
KEYPAD_KEY_9 = "9"
KEYPAD_KEY_A = "A"
KEYPAD_KEY_0 = "0"
KEYPAD_KEY_B = "B"

KEYPAD_KEY_STAR = "A"
KEYPAD_KEY_HASH = "B"

KEYPAD_R = "R"

KEYPAD_KEYS = [
	KEYPAD_KEY_1,
	KEYPAD_KEY_2,
	KEYPAD_KEY_3,
	KEYPAD_KEY_4,
	KEYPAD_KEY_5,
	KEYPAD_KEY_6,
	KEYPAD_KEY_7,
	KEYPAD_KEY_8,
	KEYPAD_KEY_9,
	KEYPAD_KEY_STAR,
	KEYPAD_KEY_0,
	KEYPAD_KEY_HASH,
    KEYPAD_R
]

# -----------------

AUDIO_PAD_SEQ_ORDER = [
	KEYPAD_KEY_1,
	KEYPAD_KEY_2,
	KEYPAD_KEY_3,
	KEYPAD_KEY_4,
	KEYPAD_KEY_5,
	KEYPAD_KEY_6,
	KEYPAD_KEY_7,
	KEYPAD_KEY_8,
	KEYPAD_KEY_9,
	KEYPAD_KEY_STAR,
	KEYPAD_KEY_0,
	KEYPAD_KEY_HASH
]

# -----------------

# Koko äänisegmentin kesto, tasattuna äänen alkuun ja päätettynä lopun hiljaisuudella
AUDIO_PAD_SEQ_DURATIONS = {
	KEYPAD_KEY_1: 1300,
	KEYPAD_KEY_2: 1300,
	KEYPAD_KEY_3: 1300,
	KEYPAD_KEY_4: 1400,
	KEYPAD_KEY_5: 1400,
	KEYPAD_KEY_6: 1600,
	KEYPAD_KEY_7: 1700,
	KEYPAD_KEY_8: 1600,
	KEYPAD_KEY_9: 1700,
	KEYPAD_KEY_A: 1400,
	KEYPAD_KEY_0: 1400,
	KEYPAD_KEY_B: 1400
}

# Lopun hiljaisuuden kesto
AUDIO_PAD_SEQ_SILENCES = {
	KEYPAD_KEY_1: 200,
	KEYPAD_KEY_2: 500,
	KEYPAD_KEY_3: 200,
	KEYPAD_KEY_4: 200,
	KEYPAD_KEY_5: 200,
	KEYPAD_KEY_6: 700,
	KEYPAD_KEY_7: 700,
	KEYPAD_KEY_8: 600,
	KEYPAD_KEY_9: 600,
	KEYPAD_KEY_A: 600,
	KEYPAD_KEY_0: 900,
	KEYPAD_KEY_B: 200
}

# -----------------
# Äänisegmenttien aloitusajat
AUDIO_PAD_SEQ_STARTS = {};

prev_key = None;
for key in AUDIO_PAD_SEQ_ORDER:
	if key == AUDIO_PAD_SEQ_ORDER[0]:
		AUDIO_PAD_SEQ_STARTS[ key ] = 0;
	else:
		AUDIO_PAD_SEQ_STARTS[ key ] = AUDIO_PAD_SEQ_STARTS[ prev_key ] + AUDIO_PAD_SEQ_DURATIONS[ prev_key ];
	prev_key = key;

# -----------------
# Äänisegmenttien lopetusajat
AUDIO_PAD_SEQ_ENDS = {};

for key in AUDIO_PAD_SEQ_ORDER:
	AUDIO_PAD_SEQ_ENDS[ key ] = AUDIO_PAD_SEQ_STARTS[ key ] + AUDIO_PAD_SEQ_DURATIONS[ key ] - AUDIO_PAD_SEQ_SILENCES[ key ];

# -----------------
# Äänisegmentit
# AUDIO_PAD = {}
#
# for key in AUDIO_PAD_SEQ_ORDER:
#     AUDIO_PAD[ key ] = sound[ AUDIO_PAD_SEQ_STARTS[ key ] : AUDIO_PAD_SEQ_ENDS[ key ] ]


# --------------------
# @TODO: Siivoa erilaiset nimeämiskonventiot
PIN_KEYBOARD_1 = -1  # ? 
PIN_KEYBOARD_2 = -2  # ? 

PIN_KEYBOARD_3 = 27 # C2
PIN_KEYBOARD_4 = 17 # C1

PIN_KEYBOARD_5 = 4  # R4
#PIN_KEYBOARD_6 = 10 # C3
#PIN_KEYBOARD_6 = 9 # C3
PIN_KEYBOARD_6 = 11 # C3

PIN_KEYBOARD_7 = 0  # R3
PIN_KEYBOARD_8 = 5  # R2
PIN_KEYBOARD_9 = 6  # R1


PIN_KEYBOARD_ANYKEY = PIN_KEYBOARD_1
PIN_KEYBOARD_GROUND = PIN_KEYBOARD_2
PIN_KEYPAD_ANYKEY = PIN_KEYBOARD_ANYKEY
PIN_KEYPAD_GROUND = PIN_KEYBOARD_GROUND


PIN_KEYPAD_C1 = PIN_KEYBOARD_3
PIN_KEYPAD_C2 = PIN_KEYBOARD_4
PIN_KEYPAD_C3 = PIN_KEYBOARD_6

PIN_KEYPAD_R1 = PIN_KEYBOARD_9
PIN_KEYPAD_R2 = PIN_KEYBOARD_8
PIN_KEYPAD_R3 = PIN_KEYBOARD_7
PIN_KEYPAD_R4 = PIN_KEYBOARD_5


KEYPAD_COLS_PINS = [ PIN_KEYPAD_C1, PIN_KEYPAD_C2, PIN_KEYPAD_C3 ]
KEYPAD_ROWS_PINS = [ PIN_KEYPAD_R1, PIN_KEYPAD_R2, PIN_KEYPAD_R3, PIN_KEYPAD_R4 ]


PIN_KEYBOARD_GPIO_INPUTS = [
	PIN_KEYBOARD_1,
	# PIN_KEYBOARD_2, Kaikki paitsi Ground
	PIN_KEYBOARD_3,
	PIN_KEYBOARD_4,
	PIN_KEYBOARD_5,
	PIN_KEYBOARD_6,
	PIN_KEYBOARD_7,
	PIN_KEYBOARD_8,
	PIN_KEYBOARD_9
]

# --------------------

PIN_SWITCH_INPUT = 23

PIN_STATUS_LED = 13

# --------------------

operationalPinsTable = [

	PIN_SWITCH_INPUT,
	PIN_STATUS_LED,

	PIN_KEYPAD_C1,
	PIN_KEYPAD_C2,
	PIN_KEYPAD_C3,

	PIN_KEYPAD_R1,
	PIN_KEYPAD_R2,
	PIN_KEYPAD_R3,
	PIN_KEYPAD_R4,

	PIN_KEYPAD_ANYKEY,
	PIN_KEYPAD_GROUND
]
if len(operationalPinsTable) != len(set(operationalPinsTable)):
	raise Exception( 'duplicate operational pins!' )

# --------------------

reverseTable = dict()

reverseTable[PIN_SWITCH_INPUT]    = 'PIN_SWITCH_INPUT'
reverseTable[PIN_KEYBOARD_1]      = 'PIN_KEYBOARD_1'
reverseTable[PIN_KEYBOARD_2]      = 'PIN_KEYBOARD_2'
reverseTable[PIN_KEYBOARD_3]      = 'PIN_KEYBOARD_3'
reverseTable[PIN_KEYBOARD_4]      = 'PIN_KEYBOARD_4'
reverseTable[PIN_KEYBOARD_5]      = 'PIN_KEYBOARD_5'
reverseTable[PIN_KEYBOARD_6]      = 'PIN_KEYBOARD_6'
reverseTable[PIN_KEYBOARD_7]      = 'PIN_KEYBOARD_7'
reverseTable[PIN_KEYBOARD_8]      = 'PIN_KEYBOARD_8'
reverseTable[PIN_KEYBOARD_9]      = 'PIN_KEYBOARD_9'
reverseTable[PIN_STATUS_LED]      = 'PIN_STATUS_LED'
reverseTable[PIN_KEYBOARD_ANYKEY] = 'PIN_KEYBOARD_ANYKEY'
reverseTable[PIN_KEYBOARD_GROUND] = 'PIN_KEYBOARD_GROUND'
