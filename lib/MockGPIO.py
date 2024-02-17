import csv

from lib.logger import debug

from lib.KeypadHandler import pad_2_c_r_2

import lib.const as const

def pinToString( pin ):
    if pin in const.reverseTable:
        return f'{ const.reverseTable[pin] }={ pin }'
    else:
        return str( pin );


class MockGPIO:

    BCM      = "BCM"
    IN       = "IN"
    OUT      = "OUT"
    HIGH     = 1
    LOW      = 0
    PUD_DOWN = "PUD_DOWN"
    RISING   = "RISING"
    FALLING  = "FALLING"
    BOTH     = "BOTH"

    def add_event_detect( self, pin, mode, **kwargs ):
        debug("MockGPIO.add_event_detect(", pin, ",", mode, ",", kwargs, ")")

    def setmode(self, mode):
        debug("MockGPIO.setmode(", mode, ")")

    def setwarnings(self, mode):
        debug("MockGPIO.setwarnings(", mode, ")")

    def setup(self, pin, mode, **kwargs):
        debug("MockGPIO.setup(", pinToString(pin), ",", mode, ")")

    def input(self, pin):
        #debug("MockGPIO.input(", pinToString(pin), ")")

        if pin in self.mock_statuses:
            return self.mock_statuses[ pin ]
        
        return self.LOW

    def output(self, pin, mode):
        #debug("MockGPIO.output(", pinToString(pin), ",", mode, ")")

        self.mock_statuses[ pin ] = mode

    def cleanup(self):
        debug("MockGPIO.cleanup()")

    def __init__(self):
        debug("MockGPIO.__init__()")

    def iterate( self ):
        pass


class FileMockGPIO(MockGPIO):

    mock_filename = "GPIO.csv"
    mock_statuses = dict()
    mock_pads     = []

    def __init__(self):
        pass

    def input(self, pin):
        #debug("FileMockGPIO.input(", pinToString(pin), ")")

        t_char = self.mock_pads[0] if len(self.mock_pads) > 0 else '?'
        if t_char in const.AUDIO_PAD_SEQ_ORDER:
            t_col, t_row = pad_2_c_r_2( t_char )

            t_c_pin = const.KEYPAD_COLS_PINS[ t_col ]
            t_r_pin = const.KEYPAD_ROWS_PINS[ t_row ]

            if pin in const.KEYPAD_ROWS_PINS:
                if self.mock_statuses[ t_c_pin ]:
                    if pin == t_r_pin:
                        return self.HIGH
                return self.LOW

        if pin in self.mock_statuses:
            return self.mock_statuses[ pin ]
        
        return self.LOW

    def iterate( self ):
        with open( self.mock_filename, 'r') as file:
            reader = csv.reader(file)
            linenum = 0
            self.mock_pads = []
            for row in reader:

                linenum+=1

                if linenum > 1 and len(row) > 2:

                    target = row[1].strip()
                    value = row[2].strip()

                    if target[0:4] == "PIN_":
                        pin  = int( target[4:] )

                        value = self.HIGH if value == '1' else self.LOW
                        self.output( pin, value )

                    elif target in const.AUDIO_PAD_SEQ_ORDER:
                        if value == '1':
                            self.mock_pads.append( target )
                        pass
                    else:
                        debug( "FileMockGPIO.iterate() Unknown target", target, ":", value )
