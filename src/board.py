import pieces as piece_src
import logic
import copy

class Board:
	pieces = []
	squares = []

	def __init__(self,size):
		self.squares = self.make_board(size)

	def get_colour_positions(self,colour):
		positions = []
		for piece in self.pieces:
			if piece.colour == colour and piece.is_alive:
				positions.append(piece.position)
		return positions
	
	def get_all_positions(self):
		black_positions = self.get_colour_positions("black")
		white_positions = self.get_colour_positions("white")
		all_positions = copy.deepcopy(white_positions)
		all_positions.extend(black_positions)
		return all_positions

	def make_board(self,size):
		squares = []

		for x in range(size[0]):
			for y in range(size[1]):
				squares.append([x+1,y+1])

		return squares
		
	def setup_board(self):
		for colour in ["white","black"]:
			self.make_pawns(colour)
			self.make_rooks(colour)
			self.make_knights(colour)
			self.make_bishops(colour)
			self.make_king(colour)
			self.make_queen(colour)
	
	def move_one_forward(self,square,delta):
		square[0] += logic.sign(offset[0])
		square[1] += logic.sign(offset[1])
		return square

	
	def remove_blocked_squares(self,piece,valid_squares):
		# will allow you to land on a square if it HAS a piece, 
		# then later on check it its enemy or not

		#doesnt work for knights
		all_positions = self.get_all_positions()
		for square in valid_squares:
			self.is_piece_between(square,piece)

	def is_piece_between(self,square,piece):
		'''
		between the square and piece including the landing square
		'''
		delta_x = square[0] - piece.position[0]
		delta_y = square[1] - piece.position[1]
		delta = (delta_x,delta_y)


		square_in_path = copy.deepcopy(piece.position)	
		square_in_path = self.move_one_forward(sqaure_in_path,delta)
	
		while square_in_path != end_position:
			if sqaure_in_path in all_positions:
				return True
			square_in_path = self.move_one_forward(square_in_path, delta)
			return False
				
	def get_valid_squares(self,piece):
		piece_offsets = piece.get_offsets()
		valid_squares = piece.get_squares_from_offsets()
		self.remove_blocked_squares(piece,valid_squares)




	def make_pawns(self, colour):
		for i in range(8):
			new_pawn = piece_src.Pawn("pawn", colour)
			self.pieces.append(new_pawn)
			current_pawn = self.pieces[-1]
			current_pawn.position = [i, current_pawn.get_nth_row(colour,2)]

	def make_rooks(self,colour):
		for i in [1,8]:
			self.pieces.append(piece_src.Rook("rook",colour))
			current_rook = self.pieces[-1]
			current_rook.position = [i, current_rook.get_nth_row(colour,1)]

	def make_knights(self,colour):
		for i in [2,7]:
			self.pieces.append(piece_src.Knight("knight", colour))
			current_knight = self.pieces[-1]
			current_knight.position = [i, current_knight.get_nth_row(colour,1)]

	def make_bishops(self,colour):
		for i in [3,6]:
			self.pieces.append(piece_src.Bishop("bishop", colour))
			current_bishop = self.pieces[-1]
			current_bishop.position = [i, current_bishop.get_nth_row(colour,1)]

	def make_king(self,colour):
		self.pieces.append(piece_src.King("king", colour))
		king = self.pieces[-1]
		king.position = [5, king.get_nth_row(colour,1)]

	def make_queen(self, colour):
		self.pieces.append(piece_src.Queen("queen",colour))
		queen = self.pieces[-1]
		queen.position = [4,queen.get_nth_row(colour,1)]





