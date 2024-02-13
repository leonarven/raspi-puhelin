import sys
import time

sys.path.append( './lib' )

from logger import debug
import audio
from GPIO import GPIO
import Switch
import Operator
import Feature
import Event
import KeypadPinger
import KeypadHandler
import const


class HandsetActionFeature( Feature.BaseHandsetActionFeature ):

    def __init__( self, events ):
        super().__init__( events )

        audio.initializeAudio( const.AUDIO_FILE_PM )
        audio.initializeAudio( const.AUDIO_FILE_LAMMAS )

    def onHandsetStatusLowered( self, data ):
        audio.playAudio( const.AUDIO_FILE_PM )

    def onHandsetStatusLifted( self, data ):
        audio.playAudio( const.AUDIO_FILE_LAMMAS )



class KeypadActionFeature( Feature.BaseKeypadActionFeature ):

    def __init__( self, events ):
        super().__init__( events )

        self.sound = audio.initializeAudio( const.AUDIO_FILE_PAD )

    def onKeypadKeydown( self, key, data ):
        super().onKeypadKeydown( key, data )
        #print("[" , str( self.iteration ).zfill( 7 ) , "]", "Detected", key )

        if key in const.AUDIO_PAD_SEQ_STARTS:
            if key in const.AUDIO_PAD_SEQ_ENDS:
                audio.playSound( const.AUDIO_FILE_PAD+"#"+key, self.sound[ const.AUDIO_PAD_SEQ_STARTS[key]:const.AUDIO_PAD_SEQ_ENDS[key] ] )



def main():
    operator = Operator.Operator()

    pinger = KeypadPinger.KeypadPinger( const.KEYPAD_ROWS_PINS, const.KEYPAD_COLS_PINS )
    keypad = KeypadHandler.KeypadHandler( pinger )

    operator.registerFeature( Feature.HandsetReaderFeature( operator.events, Switch.init() ) )
    operator.registerFeature( Feature.KeypadReaderFeature(  operator.events, keypad ) )

    operator.registerFeature( KeypadActionFeature(  operator.events ) )
    operator.registerFeature( HandsetActionFeature( operator.events ) )

    while True:
        operator.iterate()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
