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

from copy import deepcopy
# Implement the solver
class SudokuSolver:
    def __init__(self, input_path):
        # Read the input file and start the puzzle
        with open(input_path, 'r') as f:
            lines = f.readlines()
        self.cells = [list(map(int, line.split(','))) for line in lines]
    
    # Print out the initial puzzle or solution
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
    
    # To find a solution
    def solve(self):
        #First we look for a presence of a number
        def check_presence(cells):
            present_in_row = [{num: False for num in range(1, 10)} for _ in range(9)]
            present_in_column = [{num: False for num in range(1, 10)} for _ in range(9)]
            present_in_quadrant = [{num: False for num in range(1, 10)} for _ in range(9)]

            for row_id in range(9):
                for col_id in range(9):
                    temp_val = cells[row_id][col_id]
                    # If a cell is not empty, update the corresponding row, columnd and quadrant
                    if temp_val > 0:
                        present_in_row[row_id][temp_val] = True
                        present_in_column[col_id][temp_val] = True
                        present_in_quadrant[row_id // 3 * 3 + col_id // 3][temp_val] = True
            
            return present_in_row, present_in_column, present_in_quadrant
        
        # Next, a dictionary for empty locations and their possible values
        def get_possible_values(cells):
            present_in_row, present_in_column, present_in_quadrant = check_presence(cells)
            possible_values = {}
            for row_id in range(9):
                for col_id in range(9):
                    temp_val = cells[row_id][col_id]
                    if temp_val == 0:
                        possible_values[(row_id, col_id)] = []

                        # If a number is not present in the same row, column, or quadrant as an empty cell, add it to the list of possible values of that cell
                        for num in range(1, 10):
                            if (not present_in_row[row_id][num]) and (not present_in_column[col_id][num]) and (not present_in_quadrant[row_id // 3 * 3 + col_id // 3][num]):
                                possible_values[(row_id, col_id)].append(num)
            return possible_values
        
        # Fill in empty cells that have only one possible value
        def simple_update(cells):
            update_again = False
            possible_values = get_possible_values(cells)

            for row_id, col_id in possible_values:
                if len(possible_values[(row_id, col_id)]) == 1:
                    update_again = True
                    cells[row_id][col_id] = possible_values[(row_id, col_id)][0]
            
            # Recursively update with potentially new possible values
            if update_again:
                cells = simple_update(cells)

            return cells
        
        # Recursively solve the puzzle
        def recursively_solve(cells):
            cells = simple_update(cells)
            possible_values = get_possible_values(cells)
            if len(possible_values) == 0:
                return cells #returns when all cells are filled
            
            # Find the empty cell with fewest possible values
            fewest_num_values = 10
            for row_id, col_id in possible_values:
                if len(possible_values[(row_id, col_id)]) == 0:
                    return False # return if an empty is invalid
                if len(possible_values[(row_id, col_id)]) < fewest_num_values:
                    fewest_num_values = len(possible_values[(row_id, col_id)])
                    target_location = (row_id, col_id)
            
            for value in possible_values[target_location]:
                dup_cells = deepcopy(cells)
                dup_cells[target_location[0]][target_location[1]] = value
                potential_solution = recursively_solve(dup_cells)

                # Return immediately when a valid solution is found
                if potential_solution:
                    return potential_solution
            
            return False # Retrun if no valid solution is found
        
        print('Initial puzzle')
        self.display_cell()

        final_solution = recursively_solve(self.cells)
        if final_solution is False:
            print('A solution cannot be found')
        else:
            self.cells = final_solution
            print('Final Solution:')
            self.display_cell()

solver = SudokuSolver('sudoku_input/sudoku_input_2.txt')
#solver = SudokuSolver('sudoku_input/sudoku_input_1.txt')
solver.solve()