from gui import GUI
from sudoku import Sudoku

if __name__ == '__main__':

	# Create sudoku board
	sudoku = Sudoku()

	print(sudoku.board)

	# Toogle this for show/hide step-by-step solution
	step_by_step = True

	# Run with GUI	
	GUI(sudoku, step_by_step).run()