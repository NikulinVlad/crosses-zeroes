class CAZ:
	def __init__(self, s: int=3, fp: bool=1):
		self.gameBoard = [['n' for x in range(s)] for y in range(s)]
		self.fp = fp
		self.s = s
		self.m = 0
		self.win = 'n'

	def restart_game(self):
		self.gameBoard = [['n' for x in range(self.s)] for y in range(self.s)]
		self.m = 0
		self.win = 'n'

	def check_win(self):
		for y in range(self.s):
			arr = self.gameBoard[y]
			if arr.count(self.gameBoard[y][0]) == self.s and 'n' not in arr: 
				return arr[0]

		for x in range(self.s):
			arr = [self.gameBoard[y][x] for y in range(self.s)]
			if arr.count(self.gameBoard[0][x]) == self.s and 'n' not in arr:
				return arr[0]

		arr = [self.gameBoard[ind][ind] for ind in range(self.s)]
		if arr.count(self.gameBoard[0][0]) == self.s and 'n' not in arr:
			return arr[0]

		arr = [self.gameBoard[ind][self.s-1-ind] for ind in range(self.s)]
		if arr.count(self.gameBoard[0][self.s-1]) == self.s and 'n' not in arr:
			return [0]

		if self.s*self.s <= self.m:
			return 'd'

		return 'n'

	def add_fig(self, x: int, y: int):
		if self.win == 'n' and self.gameBoard[y][x] == 'n':
			self.gameBoard[y][x] = {0: 'z', 1: 'c'}.get(self.fp)
			self.fp = not self.fp
			self.m += 1

			res = self.check_win()

			if res != 'n':
				self.win = res

	def return_winner(self):
		return self.win

	def return_player_turn(self):
		return {0: 'z', 1: 'c'}.get(self.fp)

	def return_gameboard(self):
		return self.gameBoard

	def print_gameboard(self):
		for y in range(self.s):
			lineStr = str()
			for x in range(self.s):
				lineStr += f' { {"z": "o", "c": "x", "n": " "}.get(self.gameBoard[y][x]) } |'
				if x == self.s - 1:
					lineStr = lineStr[:-2]
			print(lineStr)
			if y < self.s - 1:
				print(f'{"---+"*(self.s-1)}---')
