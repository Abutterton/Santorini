import board
import action

class State(board.Board):

	def getPossibleActions(self):
		return [action.Action(self.currentPlayer, x[0], x[1], x[2]) for x in self.findMoves()]

	def takeAction(self, action):
		return State(self.getResult(action.start, action.to, action.build).state, self.getResult(action.start, action.to, action.build).currentPlayer)

	def isTerminal(self):
		return (self.winner() != "_") or (len(self.getPossibleActions()) == 0)

	def getReward(self):
		if (len(self.getPossibleActions()) == 0) or (self.winner() == 'b'):
			if self.currentPlayer == 'a':
				return -1
			else:
				return 1
		elif self.winner() == 'a':
			return 1
		else:
			return False
