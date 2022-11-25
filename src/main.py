import app as app_src
import output as out

def main():
	winner, reason = app_src.get_winner()
	out.game_over(winner,reason)

