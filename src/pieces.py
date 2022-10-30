from enum import Enum

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
		self.forward_direction = self.get_forward_direction()
		self.is_first_move = self.check_if_first_move(is_first_move)
		self.is_alive = check_is_alive(is_alive)

	class colour(Enum):
		BLACK
		WHITE

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

	def move(self, newPosition, enemy_player): #this method may be better in the player class
		#since it handles stuff involving all pieces
		self.remove_captured_pieces() #remove captured pieces if there are eny
	###check if the move was an en passant capture too 
		piece.position = position
		if piece.first_move == True:
			piece.first_move = False



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
