import pydub
import pydub.playback
import sys

# -----------------

sys.path.append('.')

import lib.audio as audio

audio.playPadAudioSequence( "0407625990" )

exit()

# -----------------

noise = pydub.generators.WhiteNoise()
noise_sound = noise.to_audio_segment( duration=1000,volume=0 )[:100]

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
