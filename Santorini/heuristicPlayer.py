import player
import random


class HeuristicPlayer(player.Player):

	def place(self, board):
		choice =  random.choice(board.findOpenPlaces())
		return choice


	def move(self, board, currentPlayer):
		moves = board.findMoves()
		currentVal = -1
		bestMoves = []
		for move in moves:
			value = self._value(board.getResult(*move))
			if value > currentVal:
				bestMoves = [move]
			elif value == currentVal:
				bestMoves.append(move)
		choice = random.choice(bestMoves)
		print('value of this move is ' + str(self._value(board.getResult(*choice))))
		return choice


	def _value(self, board):
		value = 0
		state = board.getState()
		for x in range (0,5):
			for y in range (0,5):
				if state[x][y]['player'] == self.id:
					height = state[x][y]['height']
					value += height**2
		return value




