class Player:
	enemy_player: Player
	alive_pieces = []

	def move(self, piece, target_position): 
		self.remove_captured_pieces()
		piece.position = position
		if piece.first_move == True:
			piece.first_move = False

	def remove_captured_pieces(self):
		pass

class Square:
	position = [0,0]
	piece: Piece

	def __init__(self, position):
		self.positon = position

class Board:
	squares = []
	def __init__(self,size):
		self.squares = makeBoard(size)

	def makeBoard(size):
		squares = [[]]

		for x in range(size[0]):
			for y in range(size[1]):
				square = Square([x,y])
				squares.append(square)

		return squares

def setup_board():
	board = Board([8,8])

	white_pieces = make_pieces("white")
	black_pieces = make_pieces("black")


def make_pieces(colour):
	pieces = []
	for i in range(8):
		pieces.append(pieces.Pawn("pawn", colour))

	for i in range(2):
		pieces.append(pieces.Knight("knight", colour))
		pieces.append(pieces.Rook("rook",colour))
		pieces.append(pieces.Bishop("bishop",colour))

	pieces.append(pieces.Queen("queen",colour))
	pieces.append(pieces.King("king",colour))

	return pieces

def set_piece_positions(white_pieces,black_pieces):
	# go through 2nd row and add pawns
	for square in board:
		if 