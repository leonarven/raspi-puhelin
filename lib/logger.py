import lib.const as const

def debug( *objects ):
	if const.DEBUG:
		print( *objects )