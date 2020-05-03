import numpy, boards, pygame

class Sudoku:

	def __init__(self):

		# Get random board
		self.board = boards.get_board()

	# Check if value is valid for row
	def is_valid(self, row):

	    # Get all duplicate values for row
	    u, c = numpy.unique(row, return_counts = True)
	    dup = u[c > 1]

	    # Ignore 0 (zero) value
	    return not dup.size > 1 if numpy.isin(0, dup) else not dup.size > 0

	# Check if value is valid for row
	def check_row(self, value, x, y, board = None):

	    row = board[x] if board is not None else self.board[x]
	    row[y] = value

	    return self.is_valid(row)

	# Check if value is valid for column
	def check_column(self, value, x, y):

	    # Transpose the matrix
	    t_board = self.board.transpose()

	    # Check row
	    return self.check_row(value, y, x, t_board)

	# Check if value is valid for square
	def check_square(self, value, x, y):

	    square = []
	 
	    # Arrange square into a row
	    for i in range(3):
	        for j in range(3):
	            square = numpy.append(square, self.board[3 * (x // 3) + i][3 * (y // 3) + j])

	    square[3 * (x % 3) + (y % 3)] = value

	    return self.is_valid(square)

	# Check if all rules are True
	def check(self, value, x, y):

		if self.check_row(value, x, y):
			if self.check_column(value, x, y):
				if self.check_square(value, x, y):
					return True

		return False

	# Update value (x, y)
	def update(self, value, x, y):
		
		self.board[x][y] = value

	# Solve the position of the board using backtrancking algorithm
	def solve(self, x = 0, y = 0, gui = None):

		# Base case: Complete the board
		if x == self.board[0].size:
			return self.board

		# Empty position
		if self.board[x][y] == 0:

			# Try to solve the position of board from 1 to 9
			for value in xrange(1,10):

				# Check if all rules are True
				checked = self.check(value, x, y)

				# Draw if game has GUI
				if gui is not None:
					self.draw_gui(value, x, y, gui, checked)

				if checked:
					self.board[x][y] = value

					# Try to solve the next one
					result = self.solve_next(x, y, gui)

					if result is not None:
						return result

			# Wrong solution! Reset position to empty
			else:
				self.board[x][y] = 0

				# Draw if game has GUI
				if gui is not None:
					self.draw_gui('', x, y, gui)

	    # Position is already solved, go to the next one
		else:        
			return self.solve_next(x, y, gui)

	# Solve the next position of the board
	def solve_next(self, x, y, gui):

		if y < (self.board[0].size - 1):
			return self.solve(x, y + 1, gui)
		else:
			return self.solve(x + 1, 0, gui)

	# Draw if game has GUI
	def draw_gui(self, value, x, y, gui, checked = False):

		pos = 9 * x + y

		# Update value of input box 
		gui.board[pos].text = str(value)

		# Update value setting color
		gui.board[pos].update(checked)

		# Draw input box
		gui.board[pos].draw(gui.screen)

		# Update screen
		pygame.display.update()