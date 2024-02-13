import pydub
import pydub.playback

# -----------------

import os
import sys
script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..' )
sys.path.append( mymodule_dir )


from const import AUDIO_FILE_PAD

# -----------------

sound = pydub.AudioSegment.from_file( AUDIO_FILE_PAD )

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
AUDIO_PAD = {}

for key in AUDIO_PAD_SEQ_ORDER:
    AUDIO_PAD[ key ] = sound[ AUDIO_PAD_SEQ_STARTS[ key ] : AUDIO_PAD_SEQ_ENDS[ key ] ]

# -----------------

import pydub.generators
noise = pydub.generators.WhiteNoise()
sound = noise.to_audio_segment( duration=1000,volume=0 )
noise_sound = sound[:100]

# -----------------

playPadAudio = lambda key: pydub.playback.play( AUDIO_PAD[ key ] )
playPadAudioSequence = lambda sequence: [ playPadAudio( key ) for key in sequence ]

# -----------------

print( "start" )

pydub.playback.play( noise_sound )
playPadAudio( "1" )
pydub.playback.play( noise_sound )
playPadAudio( "2" )
pydub.playback.play( noise_sound )
playPadAudio( "3" )
pydub.playback.play( noise_sound )
playPadAudio( "4" )
pydub.playback.play( noise_sound )
playPadAudio( "5" )
pydub.playback.play( noise_sound )

#playPadAudioSequence( "0407625990" )
#playPadAudioSequence( "0400582812" )



#playPadAudio( "1" )
if False:
    import time
    playPadAudio( "1" )
    time.sleep(0.1)
    playPadAudio( "2" )
    time.sleep(0.1)
    playPadAudio( "3" )
    time.sleep(0.1)
    playPadAudio( "4" )
    time.sleep(0.1)
    playPadAudio( "5" )
    time.sleep(0.1)
    playPadAudio( "6" )
    time.sleep(0.1)
    playPadAudio( "7" )