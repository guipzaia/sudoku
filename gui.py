import pygame
from pygame import *

import color

from inputbox import InputBox

class GUI:

	def __init__(self, sudoku, step_by_step):

		pygame.init()

		self.title = 'Sudoku'

		pygame.display.set_caption(self.title)

		self.screen_size = 900
		self.border = 2
		self.squares = [
			(self.screen_size // 3) - (2 * self.border),
			(self.screen_size // 9) - (2 * self.border)
		]
		self.screen = pygame.display.set_mode((self.screen_size, self.screen_size))

		self.screen.fill(color.BLACK)
		self.sudoku = sudoku
		self.board = self.init_board()
		self.step_by_step = step_by_step

	# Init GUI board 
	def init_board(self):

		board = []

		for x in range(0, self.screen_size, self.screen_size // 9):

			for y in range(0, self.screen_size, self.screen_size // 9):

				# Draw border of the squares
				if x % 3 == 0 and y % 3 == 0:
					pygame.draw.rect(self.screen, color.GRAY,
						Rect(x + self.border, y + self.border, self.squares[0], self.squares[0]))

				num = self.sudoku.board[x // 100][y // 100]

				# Create input boxes
				if num > 0:
					inputbox = InputBox(x, y, self.squares[1], self.squares[1], self.border, str(num), True)
				else:
					inputbox = InputBox(x, y, self.squares[1], self.squares[1], self.border)

				# Append new InputBox into an array
				board.append(inputbox)

		return board

	# Run the game
	def run(self):

		clock = pygame.time.Clock()

		# Draw all input boxes on screen
		for inputbox in self.board:
			inputbox.draw(self.screen)

		# Game looping
		while True:

			# Handle events
			for event in pygame.event.get():

				# Quit the game
				if event.type == pygame.QUIT:
					pygame.quit()

				elif event.type == pygame.KEYDOWN:

					# Solve game
					if event.key == pygame.K_SPACE:
						self.solve()

				# Handle input box event
				self.handle_inputbox(event)

			# Update sreen
			pygame.display.update()

			clock.tick(50)

	# Solve the game using backtracking
	def solve(self):

		print('Solving game using backtracking algorithm...')

		# Display step by step of solution
		if self.step_by_step:
			print(self.sudoku.solve(0, 0, self))

		# Display only solved board
		else:
			print(self.sudoku.solve())

			for x in range(9):
				for y in range(9):

					inputbox = self.board[9 * x + y]

					if not inputbox.block:

						# Update value of input box 
						inputbox.text = str(self.sudoku.board[x][y])

						# Update value setting color
						inputbox.update(True)

						# Draw input box
						inputbox.draw(self.screen)

	# Handle input box event
	def handle_inputbox(self, event):

		for inputbox in self.board:

			(n, x, y) = inputbox.handle_event(event)

			if n is not None and x is not None and y is not None:

				# Update value of input box setting color
				inputbox.update(self.sudoku.check(int(n), x // 100, y // 100))

				# Update value of sudoku board 
				self.sudoku.update(int(n), x // 100, y // 100)

			# Draw input box
			inputbox.draw(self.screen)