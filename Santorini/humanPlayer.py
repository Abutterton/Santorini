import player

class HumanPlayer(player.Player):

	def place(self, board):
		move = input(f"Player {self.id}, where do you want to place your peice?")
		return tuple(int(x) for x in move.split(','))


	def move(self, board, currentPlayer):
		peice = input(f"Player {self.id}, what peice do you want to move?")
		peiceTup = tuple(int(x) for x in peice.split(','))

		moveTo = input(f"Player {self.id}, where do you want to move to?")
		moveToTup = tuple(int(x) for x in moveTo.split(','))

		build = input(f"Player {self.id}, where do you want to build?")
		buildTup = tuple(int(x) for x in build.split(','))

		return (peiceTup,moveToTup,buildTup)

