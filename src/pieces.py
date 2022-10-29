class piece:
	name: str
	position: [0,0]
	is_first_move: bool
	is_alive: bool
	colour: str

	def __init__(self, name, position, colour, is_first_move = None, is_alive = None):
		self.name = name
		self.position = position
		self.colour = colour
		self.is_first_move = check_if_first_move(is_first_move)
		self.is_alive = check_is_alive(is_alive)
	
	def check_if_first_move(is_first_move):
		if is_first_move is None:
			return True
		else:
			return is_first_move

	def check_is_alive(is_alive):
		if is_alive is None:
			return True
		else:
			return is_alive


class king(piece):
	def __init__(self, name, position, colour, is_first_move = None, is_alive = None):
		super.__init__(self, name, position, colour, is_first_move = None, is_alive = None)

class queen(piece):
		def __init__(self, name, position, colour, is_first_move = None, is_alive = None): 
			super.__init__(self, name, position, colour, is_first_move = None, is_alive = None)

class pawn(piece):
	def __init__(self, name, position, colour, is_first_move = None, is_alive = None): 
			super.__init__(self, name, position, colour, is_first_move = None, is_alive = None)

class rook(piece):
	def __init__(self, name, position, colour, is_first_move = None, is_alive = None): 
			super.__init__(self, name, position, colour, is_first_move = None, is_alive = None)

class bishop(piece):
	def __init__(self, name, position, colour, is_first_move = None, is_alive = None): 
			super.__init__(self, name, position, colour, is_first_move = None, is_alive = None)

class knight(piece):
	def __init__(self, name, position, colour, is_first_move = None, is_alive = None): 
			super.__init__(self, name, position, colour, is_first_move = None, is_alive = None)
