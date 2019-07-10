# A class that represents the current game state


class Board:

	def __init__(self, state=None, currentPlayer=1):
		if state:
			self.state = [[{'height': y.get('height'), 'player': y.get(
			    'player')} for y in x] for x in state]
			self.currentPlayer = currentPlayer
		else:
			self.state = [[{'height': 0, 'player': '_'}
			    for x in range(0, 5)] for x in range(0, 5)]
			self.currentPlayer = currentPlayer

	def place(self, coordinate):
		if self._isOpenPlace(coordinate):
			if self.currentPlayer == 1:
				self.state[coordinate[0]][coordinate[1]]['player'] = 'a'
			else:
				self.state[coordinate[0]][coordinate[1]]['player'] = 'b'
			self.currentPlayer = self.currentPlayer * -1
		else:
			raise ValueError('invalid placement')
		# self.printBoard()
		# print()

	def getState(self):
		return self.state

	def move(self, currentLoc, destinationLoc, buildLoc):
		if (self._isLegalMove(currentLoc, destinationLoc, buildLoc)):
			self.state[destinationLoc[0]][destinationLoc[1]
			    ]['player'] = self.state[currentLoc[0]][currentLoc[1]].get('player')
			self.state[currentLoc[0]][currentLoc[1]]['player'] = '_'
			self._build(buildLoc)
			self.currentPlayer = self.currentPlayer * -1
		else:
			raise ValueError('invalid move')

	def getResult(self, currentLoc, destinationLoc, buildLoc):
		returnState = Board(self.state, self.currentPlayer)
		if (self._isLegalMove(currentLoc, destinationLoc, buildLoc)):
			returnState.state[destinationLoc[0]][destinationLoc[1]
			    ]['player'] = returnState.state[currentLoc[0]][currentLoc[1]].get('player')
			returnState.state[currentLoc[0]][currentLoc[1]]['player'] = '_'
			returnState._build(buildLoc)
			# returnState.printBoard()
			# print()
			returnState.currentPlayer = returnState.currentPlayer * -1
			return returnState
		else:
			raise ValueError('invalid move')

	def printBoard(self):
		for x in range(0, 5):
			line = ""
			for y in range(0, 5):
				line = line + str(self.state[x][y].get('height')) + \
				                  self.state[x][y].get('player') + " "
			print(line)

	def findOpenPlaces(self):
		locs = []
		for x in range(0, 4):
			for y in range(0, 4):
				if self._isOpenPlace((x, y)):
					locs.append((x, y))
		return locs

	def findMoves(self):
		moves = []
		peices = self._findPeices()
		for p in peices:
			possibleDestination = []
			for x in range(0, 5):
				for y in range(0, 5):
					if self._isAdjacent(
    p, (x, y)) and self._isOpenMove(
        (x, y)) and self._acceptableMoveHeight(
            p, (x, y)):
						possibleDestination.append((x, y))
			for d in possibleDestination:
				for a in range(0, 5):
					for b in range(0, 5):
						if self._isAdjacent(d, (a, b)) and self._isOpenBuild(p, d, (a, b)):
							moves.append((p, d, (a, b)))

		winningMoves = [x for x in moves if self.getResult(*x).winner() != '_']
		if len(winningMoves) > 0:
			return winningMoves
		else:
			return moves

	def get_previous_move(self, prevState):
		moves = prevState.findMoves()
		for move in moves:
			if prevState.getResult(*move).state == self.state:
				return move

	def winner(self):
		for x in range(0, 5):
			for y in range(0, 5):
				if (self.state[x][y]['height'] == 3) and (
				    self.state[x][y]['player'] != '_'):
					return self.state[x][y]['player']
		return '_'

	def _currentPlayerID(self):
		if self.currentPlayer == 1:
			return 'a'
		else:
			return 'b'

	def _isLegalMove(self,  currentLoc, destinationLoc, buildLoc):
		if (not self._isAdjacent(currentLoc, destinationLoc)):
			print('must select a destinationLoc must be adjacent to currentLoc')
			return False
		elif (not self._isAdjacent(buildLoc, destinationLoc)):
			print('must select a buildLoc must be adjacent to destinationLoc')
			return False
		elif (not  self._isOpenMove(destinationLoc)):
			print(f'destinationLoc blocked, {destinationLoc} is {self.state[destinationLoc[0]][destinationLoc[1]]}')
			return False
		elif (not self._acceptableMoveHeight(currentLoc,destinationLoc)):
			print('can only move up one level in a move')
			return False
		elif (not self._isOpenBuild(currentLoc, destinationLoc, buildLoc)):
			print('buildLoc blocked')
			return False
		else: 
			return True


	def _isOpenPlace(self, coordinate):
		try:
			if self.state[coordinate[0]][coordinate[1]].get('player') == '_':
				return True
			else:
				print ('location occupied')
				return False
		except IndexError as e:
			print('choose a location on the board')
			return False


	def _findPeices(self):
		locs = []
		for x in range(0,5):
			for y in range(0,5):
				if self.state[x][y]['player'] == 'a' and self.currentPlayer == 1:
					locs.append((x,y))
				elif self.state[x][y]['player'] == 'b' and self.currentPlayer == -1:
					locs.append((x,y))
		return locs


	def _build(self, coordinate): 
		self.state[coordinate[0]][coordinate[1]]['height'] = self.state[coordinate[0]][coordinate[1]].get('height') + 1

	def _isAdjacent(self, c1, c2):
		return (abs(c1[0] - c2[0]) <= 1) and (abs(c1[1] - c2[1]) <= 1)

	def _isOpenMove(self, target):
		try:
			return (self.state[target[0]][target[1]].get('player') == '_') and (self.state[target[0]][target[1]].get('height') != '4')
		except IndexError as e:
			print ("move destination out of bounds")
			return False

	def _acceptableMoveHeight(self, moveFrom,moveTo):
		return self.state[moveFrom[0]][moveFrom[1]].get('height') + 1 >= self.state[moveTo[0]][moveTo[1]].get('height')

	def _isOpenBuild(self, moveFrom, moveTo, target):
		try:
			return (self.state[target[0]][target[1]].get('height') < 4) and ((self.state[target[0]][target[1]].get('player') == '_' and (moveTo != target)) or (target == moveFrom))
		except IndexError as e:
			print ("build destination out of bounds")
			return False




