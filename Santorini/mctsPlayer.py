import montecarlo
from montecarlo.node import Node
from montecarlo.montecarlo import MonteCarlo
from copy import deepcopy
import gameManager, board, player
import sys, os

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__


class MctsPlayer(player.Player):

	def __init__(self, char, num_sims = 100):
		self.id = char
		self.num_sims = num_sims
		self.board = board.Board()
		self.root = node(board.Board(board.getState(), currentPlayer))
		santoriniSim.player_number = 2

	def init_board(state, currentPlayer):
		self.board = board.Board(state, currentPlayer)
		self.root = Node(board.Board(board.getState(), currentPlayer))
		santoriniSim.player_number = 2
		montecarlo = MonteCarlo(root)
		montecarlo.simulate(self.num_sims)


	def place(self, board):
		blockPrint()
		choice = random.choice(board.findOpenPlaces())
		enablePrint()
		return  choice


	def move(self, board, currentPlayer):
		#blockPrint()j
		print(f"mctsPlayer is searching for the best move")
		montecarlo.simulate(50)
		#enablePrint()
		chosen_child_node = montecarlo.make_choice()
		return (chosen_child_node.state.get_previous_move(self.root.state))



def child_finder(node):
	for move in node.state.getMoves():
		child = Node(deepcopy(node.state))
		child.state.move(*move)
		node.add_child(child)

def node_evaluator(self, node):
	if self.id == 'a':
		return node.state.winner()
	elif self.id =='b':
		return (-1) * node.state.winner()

montecarlo.child_finder = child_finder
montecarlo.node_evaluator = node_evaluator