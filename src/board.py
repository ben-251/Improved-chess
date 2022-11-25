import pieces as piece_src

class Board:
	pieces = []
	squares = []

	def __init__(self,size):
		self.squares = self.make_board(size)

	def make_board(self,size):
		squares = []

		for x in range(size[0]):
			for y in range(size[1]):
				squares.append([x+1,y+1])

		return squares
		
	def setup_board(self):
		self.make_pieces()

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

	def make_pieces(self):
		for colour in ["white","black"]:
			self.make_pawns(colour)
			self.make_rooks(colour)
			self.make_knights(colour)
			self.make_bishops(colour)
			self.make_king(colour)



