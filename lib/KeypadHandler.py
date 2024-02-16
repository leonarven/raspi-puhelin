from lib.const import AUDIO_PAD_SEQ_ORDER


def pad_2_c_r_2( pad ):
	n = AUDIO_PAD_SEQ_ORDER.index( pad )
	return ( n % 3, n // 3 )


def c_r_2_pad( c, r ):
	n = 3 * r + c
	return AUDIO_PAD_SEQ_ORDER[ n ] if n < 12 else None

class KeypadHandler:

	def _c_r_2_pad( self, c, r ):
		n = 3 * r + c
		return AUDIO_PAD_SEQ_ORDER[ n ] if n < 12 else None

	_multikey_fix_mapping = {
		'1A': '1',
		'12': '2',
		'13': '3',
		'4A': '4',
		'45': '5',
		'46': '6',
		'7A': '7',
		'78': '8',
		'79': '9',
		'A0': '0',
		'AB': 'B',
	}

	def _solve_multikey_fix( self, keys ):
		key_s = ''.join( keys )
		return self._multikey_fix_mapping[ key_s ] if key_s in self._multikey_fix_mapping else None

	# --------------------

	iteration = 0

	pinger = None

	def __init__( self, pinger ):
		self.pinger = pinger;
		pass


	keydetection_listener = None

	def registerKeydetectionListener( self, listener ):
		self.keydetection_listener = listener

	keypressed_listener = None

	def registerKeypressedListener( self, listener ):
		self.keypressed_listener = listener
	
	keydown_listener = None

	def registerKeydownListener( self, listener ):
		self.keydown_listener = listener

	keyup_listener = None

	def registerKeyupListener( self, listener ):
		self.keyup_listener = listener


	def iterate( self ):
		
		self.iteration += 1

		keys_by_pins = self.pinger.iterateActiveKey()
		keys = []

		for col_idx, rows in enumerate( keys_by_pins ):
			for row_idx in rows:
				keys.append( self._c_r_2_pad( col_idx, row_idx ) )

		# Ei painallusta
		if len(keys) == 0:
			self.onKeyDetected( None )
			return

		# Mahdollinen virhepainallus (tai monen napin painallus)
		if len(keys) > 1:
			fix = self._solve_multikey_fix( keys )
			if fix is not None:
				keys = [ fix ]

		# Lopulta hallussa vain lopulliset painallukset yksi painallus!
		if len(keys) == 1:

			if keys[0] is not None:

				#print( "SUCCESS :: ", keys[0] )

				self.onKeyDetected( keys[0] )

			else:
				print( "ERROR_A  ::   ", keys )
				
		else:
			print( "ERROR_B ::   ", keys )
	


	prev_keys_count = 3
	prev_keys = [ None, None, None]

	def onKeyDetected( self, key ):
		if self.keydetection_listener is not None:
			self.keydetection_listener( key )

		self.prev_keys.append( key )
		self.prev_keys = self.prev_keys[-self.prev_keys_count:]

		sum_key = key

		for k in self.prev_keys:
			if k != sum_key:
				return

		self.onKeyPressed( key )
			

	pressed_key = None

	def onKeyPressed( self, key ):
		if self.keypressed_listener is not None:
			self.keypressed_listener( key )

		if self.pressed_key == key: return

		prev_key = self.pressed_key

		self.pressed_key = key

		if key is None: # Nappia ei ole enää painettu!
			self.onKeyup( prev_key )

		elif prev_key is not None: # Äsken oli eri nappi pohjassa
			self.onKeyup( prev_key )
			self.onKeydown( key )

		else: # Ei ollut äsken mitään pohjassa
			self.onKeydown( key )


	def onKeyup( self, key ):
		if self.keyup_listener is not None:
			self.keyup_listener( key )

	def onKeydown( self, key ):
		if self.keydown_listener is not None:
			self.keydown_listener( key )
