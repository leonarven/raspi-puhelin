import sys

sys.path.append( '.' )

import lib.const as const

def debug( *objects ):
	if const.DEBUG:
		print( *objects )