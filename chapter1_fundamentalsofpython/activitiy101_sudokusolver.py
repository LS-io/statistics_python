## Here, I will be utilising some of the concepts covered so far to implement a sudoku solver
## From activity 1.01: Building a Sudoku Solver
#####################################################################################
import time
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
But you can input any dimension you want!
Input below.
""")
time.sleep(2)
N = int(input('Specify the board dimension: '))

# This prints out the empty board
def display_sudoku(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end = '')
        print()