
DEBUG = True

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

AUDIO_PAD_SEQ_ORDER = [ '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', '0', 'B' ];

# -----------------

# Koko äänisegmentin kesto, tasattuna äänen alkuun ja päätettynä lopun hiljaisuudella
AUDIO_PAD_SEQ_DURATIONS = {
    '1': 1300,
    '2': 1300,
    '3': 1300,
    '4': 1400,
    '5': 1400,
    '6': 1600,
    '7': 1700,
    '8': 1600,
    '9': 1700,
    'A': 1400,
    '0': 1400,
    'B': 1400
}

# Lopun hiljaisuuden kesto
AUDIO_PAD_SEQ_SILENCES = {
    '1': 200,
    '2': 500,
    '3': 200,
    '4': 200,
    '5': 200,
    '6': 700,
    '7': 700,
    '8': 600,
    '9': 600,
    'A': 600,
    '0': 900,
    'B': 200
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

PIN_SWITCH_INPUT = 23

PIN_KEYBOARD_1 = 3  # ? 
PIN_KEYBOARD_2 = 4  # ? 

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


PIN_STATUS_LED = 13

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
