## This problem states, that we have to find a combination of placing the queens on a chess board, so that no two queens will be able to attack each other.
## A queen can attack in its column, row and diagonal, so we essentially have to find a combination so that no two queens share the same row, column or diagonal.


# A variable to specify the size of our chessboard
N = input('Specify the size of the chessboard (number + ENTER): ')
N = int(N)

# Print out the chessboard
def display_solution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end = ' ')
        print()

# Generate a valid solution
def generate_solution():
    # Check if the queen can be placed in the position
    def check_next(board, row, col):
        # Check in the current column
        for i in range(row):
            if board[i][col] == 1:
                return False
        
        # Check the upper-left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        # Check the upper-right diagonal
        for i, j in zip(range(row, -1, -1), range(col, N)):
            if board[i][j] == 1:
                return False
        
        return True

    # Recursively generate a solution
    def recur_generate_solution(board, row_id):
        # Return if we have reached the last row
        if row_id >= N:
            return True
        
        # Iteratively try out cells in the current row
        for i in range(N):
            if check_next(board, row_id, i):
                board[row_id][i] = 1
            
                # Return if a valid solution is found
                final_board = recur_generate_solution(board, row_id + 1)
                if final_board:
                    return True
            
                board[row_id][i] = 0

        # When the current board has no valid solutions
        return False
    
    # Start out with an empty board
    my_board = [[0 for _ in range(N)] for __ in range(N)]
    final_solution = recur_generate_solution(my_board, 0)

    # Display the final solution
    if final_solution is False:
        print('A solution cannot be found')
    else:
        print('A solution was found.')
        display_solution(my_board)

generate_solution()