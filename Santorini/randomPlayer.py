import player
import random
import sys, os

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

class RandomPlayer(player.Player):

	def place(self, board):
		blockPrint()
		choice =  random.choice(board.findOpenPlaces())
		enablePrint()
		return choice

	def move(self, board, currentPlayer):
		return random.choice(board.findMoves())