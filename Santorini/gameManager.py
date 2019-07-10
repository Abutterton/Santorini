# The main program that creates and plays games of santorini
import board
import player
import randomPlayer
import humanPlayer
import mctsPlayer
import heuristicPlayer
import sys, os

from mcts import mcts


class GameManager:

    def __init__(self, p1, p2):
        """The game manager starts and runs a game of santorini

        Keyword Args:
        p1 -- the Player that will go first
        p2 -- the Player that will go second

        Return -- the player that won the game"""

        self.theBoard = board.Board()
        self.p1 = p1
        self.p2 = p2
        self.currentPlayer = 1
        self.winner = None
        self._setUp()
        self._play()


    def get_winner(self):
        """return the char of the winning player"""

        return self.winner


    def _setUp(self):
        """sequentially ask players to each place their peices"""

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
        """ask players to take turns making moves until one of them wins"""

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



# Disable
def blockPrint():
    """stop text from being printed"""
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    """allow text to be printed again"""
    sys.stdout = sys.__stdout__

def main(p1 = 'random', p2= 'random', i =1):
    """gameManager can take 3 args for the 2 kinds of players and the number of games to play

    Args:
    p1 and p2 -- can be 'human', 'random', or 'heuristic' corresponding to the 3 kinds of players
    i -- an int for the number of games to run"""

    player1Wins = 0
    totalGames = int(i)

    if p1 == "human":
        a = humanPlayer.HumanPlayer('a')
    elif p1 == "random":
        a = randomPlayer.RandomPlayer('a')
    else:
        a = heuristicPlayer.HeuristicPlayer('a')

    if p2 == "human":
        b = humanPlayer.HumanPlayer('b')
    elif p2 == "random":
        b = randomPlayer.RandomPlayer('b')
    else:
        b = heuristicPlayer.HeuristicPlayer('b')





    for i in range(totalGames):
        print(f'starting round {i}')

        blockPrint()

        game = GameManager(a, b)
        result = game.get_winner()

        enablePrint()

        if result == 'a':
            player1Wins += 1

    print(f'player 1 won {player1Wins} out of {totalGames} games')


if __name__ == '__main__':
    main(*sys.argv[1:])




