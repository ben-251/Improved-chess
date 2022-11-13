class Piece:
	name: str
	is_first_move: bool
	is_alive: bool
	colour: str

	def __init__(self, name, colour, is_first_move = None, is_alive = None):
		self.name = name
		self.colour = colour
		self.forward_direction = self.get_forward_direction() #this space is the wrong level of abstraction
		self.is_first_move = self.check_if_first_move(is_first_move)
		self.is_alive = check_is_alive(is_alive)

	def get_valid_moves(self,board):
		...

	def get_forward_direction(self):
		if self.colour == "white":
			return 1
		elif self.colour == "black":
			return -1
		else:
			raise Exception("the piece is neither white nor black!")

	def check_if_first_move(self,is_first_move):
		if is_first_move is None:
			return True
		else:
			return is_first_move

	def check_is_alive(self,is_alive):	
		if is_alive is None:
			return True
		else:
			return is_alive

class King(piece):
	def __init__(self, name, colour, is_first_move = None, is_alive = None):
		super.__init__(self, name, colour, is_first_move = None, is_alive = None)

class Queen(piece):
		def __init__(self, name, colour, is_first_move = None, is_alive = None): 
			super.__init__(self, name, colour, is_first_move = None, is_alive = None)

class Pawn(piece):
	def __init__(self, name, colour, is_first_move = None, is_alive = None): 
			super.__init__(self, name, colour, is_first_move = None, is_alive = None)

class Rook(piece):
	def __init__(self, name, colour, is_first_move = None, is_alive = None): 
			super.__init__(self, name, colour, is_first_move = None, is_alive = None)

class Bishop(piece):
	def __init__(self, name, colour, is_first_move = None, is_alive = None): 
			super.__init__(self, name, colour, is_first_move = None, is_alive = None)

class Knight(piece):
	def __init__(self, name, colour, is_first_move = None, is_alive = None): 
			super.__init__(self, name, colour, is_first_move = None, is_alive = None)
