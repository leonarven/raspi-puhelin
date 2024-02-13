
from logger import debug

import Event

class Operator:

    events = Event.Handler();

    features = []

    def __init__( self ):
        pass


    def registerFeature( self, feature ):
        self.features.append( feature )


    def iterate( self ):

        #debug( "Operator.iterate()" )

        for feature in self.features:
            feature.iterate()
