import player
import random


class RandomPlayer(player.Player):

	def place(self, board):
		choice =  random.choice(board.findOpenPlaces())
		return choice

	def move(self, board, currentPlayer):
		return random.choice(board.findMoves())