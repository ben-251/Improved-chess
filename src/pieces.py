class Piece:
	name: str
	is_first_move: bool
	is_alive: bool
	colour: str
	position =  []

	def __init__(self, name, colour, position = None, is_first_move = None, is_alive = None):
		self.name = name
		self.colour = colour
		self.position = self.set_default_position(position)
		self.is_first_move = self.check_if_first_move(is_first_move)
		self.is_alive = self.check_is_alive(is_alive)

	def move(self, board, target_position): #to fix up
		board.remove_captured_pieces()
		piece.position = position
		if piece.first_move == True:
			piece.first_move = False

	def get_valid_moves(self,board):
		...

	def get_nth_row(self,colour,n):
		return self.get_backrank(colour) + ((n-1) * self.get_forward_direction(colour))

	def get_forward_direction(self,colour):
		if colour == "white":
			return 1
		elif colour == "black":
			return -1
		else:
			raise Exception("the piece is neither white nor black!")

	def get_backrank(self,colour):
		if colour == "white":
			return 1
		elif colour == "black":
			return 8
		else:
			raise Exception("the piece is neither white nor black!")			

	def set_default_position(self,position):
		if position is None:
			return []
		else:
			return position

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

class King(Piece):
	def __init__(self, name, colour, position = None, is_first_move = None, is_alive = None):
		super().__init__(name, colour, position, is_first_move, is_alive)

class Queen(Piece):
	def __init__(self, name, colour, position = None, is_first_move = None, is_alive = None): 
		super().__init__(name, colour, position, is_first_move, is_alive)

class Pawn(Piece):
	def __init__(self, name, colour, position = None, is_first_move = None, is_alive = None): 
		super().__init__(name, colour, position, is_first_move, is_alive)

class Rook(Piece):
	def __init__(self, name, colour, position = None, is_first_move = None, is_alive = None): 
		super().__init__(name, colour, position, is_first_move, is_alive)

class Bishop(Piece):
	def __init__(self, name, colour, position = None, is_first_move = None, is_alive = None): 
		super().__init__(name, colour, position, is_first_move, is_alive)

class Knight(Piece):
	def __init__(self, name, colour, position = None, is_first_move = None, is_alive = None): 
		super().__init__(name, colour, position, is_first_move, is_alive)
