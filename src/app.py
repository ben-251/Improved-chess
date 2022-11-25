import board as board_src

class app():
	current_player = "white"
	board = self.get_board()

	def get_board(self):
		board = board_src.Board([8,8])
		board.setup_board()
		return board

	def get_winner():
		while True:
			is_mate = self.check_for_mate()
			is_draw = self.check_for_draws()
			play_next_move()
			swap_colours()

	def check_for_mate(self):
		...
	
	def check_for_draws(self):
		...

	def swap_colours(self):
		if self.current_player == "white":
			self.current_player = "black" 
		elif self.current_player == "black":
			self.current_player = "white"

