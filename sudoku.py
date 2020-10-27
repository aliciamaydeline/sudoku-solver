board_easy = [
    [0, 4, 2, 0, 0, 5, 0, 0, 6],
    [1, 9, 7, 0, 0, 0, 0, 4, 0],
    [5, 6, 0, 4, 0, 0, 1, 0, 9],
    [8, 0, 1, 3, 0, 0, 2, 6, 0],
    [9, 0, 0, 0, 7, 1, 4, 5, 0],
    [0, 0, 3, 2, 5, 6, 0, 0, 0],
    [0, 0, 5, 0, 3, 2, 7, 0, 0],
    [0, 0, 4, 5, 9, 0, 6, 0, 0],
    [0, 0, 0, 7, 6, 0, 0, 8, 0]
]


# do for medium, hard later?

def display_board(board):
    """ given the board (which is an array of 9 arrays, each small array
    represents one row in the sudoku board),
    prints a representation of the board
    """
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("\n - - - - - - - - - - - - - - - - ")

        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            elif j % 9 == 0 and i % 3 != 0:
                print("")

            if board[i][j] == 0:
                print("   ", end="")
            else:
                print(" " + str(board[i][j]) + " ", end="")

    print("")   # just to give a new line at the end


def find_next_empty(board):
    """ given the board, find the next empty space, (searching from the top-left corner,
    and going row-to-row from left to right)
    returns the coordinates for the empty space in tuple of (row, column)
    e.g. (0, 0) being the top left corner and (8, 8) being the bottom right corner
    """
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return i, j

    # board is full, return False
    return False


def check_valid(board, num, pos):
    """ given the board, returns true if the given number (num) can
    be inserted in the position (pos) and returns false otherwise
    """
    # first, check the row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # then, check the column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # then, check for every 3x3 small square
    # check where the position is (which small square)
    # each small square is defined by its top left corner position
    row = pos[0]
    col = pos[1]
    if row % 3 == 1:
        row -= 1
    elif row % 3 == 2:
        row -= 2

    if col % 3 == 1:
        col -= 1
    elif col % 3 == 2:
        col -= 2

    for i in range(row, row + 3):
        for j in range(col, col + 3):
            if board[i][j] == num and (i != pos[0] or j != pos[1]):
                return False

    return True


def solve_board(board):
    # base case: where there is no empty space left, means we're done
    empty = find_next_empty(board)
    if not empty:
        return True
    else:
        row, col = empty

    for num in range(1, 10):
        if check_valid(board, num, (row, col)):
            board[row][col] = num

            # calling on solve recursively until we're done
            # if solution is found, return True
            if solve_board(board):
                return True
            else:
                # else, backtrack, try other num
                board[row][col] = 0

    return False


display_board(board_easy)
solve_board(board_easy)
print("\n\n")
display_board(board_easy)
