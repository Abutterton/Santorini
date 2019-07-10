# The main program that creates and plays games of santorini
import board
import player
import randomPlayer
import humanPlayer
import mctsPlayer
import heuristicPlayer

from mcts import mcts

import sys, os

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

class GameManager:
    def __init__(self, p1, p2):
        self.theBoard = board.Board()
        self.p1 = p1
        self.p2 = p2
        self.currentPlayer = 1
        self.winner = None

    def start(self):
        self._setUp()
        self._play()
        return self.winner

    def _setUp(self):
        i = 0
        while i < 4:
            try:
                if self.currentPlayer == 1:
                    placement = self.p1.place(self.theBoard)
                    print(f"a placed at {placement}")
                else:
                    placement = self.p2.place(self.theBoard)
                    print(f"b placed at {placement}")
                self.theBoard.place(placement)
                self.theBoard.printBoard()
                print()
                self._nextTurn()
                i += 1
            except ValueError:
                print("Please enter a legal placement")

    def _play(self):
        while (self.theBoard.winner() == '_'):
            try:
                if self.currentPlayer == 1:
                    move = self.p1.move(self.theBoard, self.currentPlayer)
                    print(f"a moved from {move[0]} to {move[1]} and built at {move[2]}")
                else:
                    move = self.p2.move(self.theBoard, self.currentPlayer)
                    print(f"b moved from {move[0]} to {move[1]} and built at {move[2]}")
                self.theBoard.move(*move)
                self.theBoard.printBoard()
                print()
                self._nextTurn()
            except ValueError as e:
                print(e)
                print("Please enter a legal move")
            except IndexError as e:
                print(e)
                print('current player has no moves')
                self.theBoard.printBoard()
                if self.currentPlayer == 1:
                    self.winner = 'b'
                else:
                    self.winner = 'a'
                print(f"{self.winner} won!")
                return
        self.winner = self.theBoard.winner()
        print(f"{self.winner} won!")

    def _nextTurn(self):
        self.currentPlayer = self.currentPlayer * (-1)




player1Wins = 0
for i in range(1):
    print(f'starting round {i}')
    a = heuristicPlayer.HeuristicPlayer('a')
    b = heuristicPlayer.HeuristicPlayer('b')

    print("about to start game")

    result = GameManager(a, b).start()
    if result == 'a':
        player1Wins += 1

print(f'player 1 won {player1Wins} out of 1 games')
#mctsWinsCount = 0

#for i in range(5):
    #print(f'starting round {i}')
    #b = randomPlayer.RandomPlayer('b')
    #a = mctsPlayer.MctsPlayer('a')
    #game = GameManager(a, b)
    #result = game.start()
    #if result == 'a':
        #mctsWinsCount += 1

#print(f'mctsPlayer won {mctsWinsCount} out of 100 games')
