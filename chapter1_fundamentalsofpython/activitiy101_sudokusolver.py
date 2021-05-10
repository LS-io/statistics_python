## Here, I will be utilising some of the concepts covered so far to implement a sudoku solver
## From activity 1.01: Building a Sudoku Solver
#####################################################################################
## First, we need to create an empty sudoku board
## The dimension have to be square (height == length)
## In the original sudoku game, you will have squares of the length 3, comprising together a bigger square of length 9, essentially giving us an option of number from 1 to 9
##
## To conclude, we wiill be setting up a sudoku board with a dimension, that is divisible by 3 (since I want to respect the original game)
## We could do this also with any other number as a dimension, as long as the produced board is square

# The user is asked to specify the dimension of the board
print("""
Welcome to Sudoku9!
In this iteration, I will demonstrate the solver using a Sudoku board of dimension 9x9.
""")

# This generates the empty board
# def display_solved_board():
#     for i in range(9):
#         for j in range(9):
#             print(board[i][j], end = '')
#         print()
#     return

# Implement the solver
class SudokuSolver:
    def __init__(self, input_path):
        with open(input_path, 'r') as f:
            lines = f.readlines()
        self.cells = [list(map(int, line.split(','))) for line in lines]
    
    def display_cell(self):
        print('-' * 23)

        for i in range(9):
            for j in range(9):
                print(self.cells[i][j], end =' ')

                if j % 3 == 2:
                    print('|', end = ' ')
            print()

            if i % 3 == 2:
                print('-' * 23)
        print()