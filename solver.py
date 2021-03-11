from board import get_board, write_board
from helper import print_board

def get_empty():
    global board
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None

def is_valid(row, col, number):
    global board
    for i in range(9):
        if board[row][i] == number:
            return False
    for i in range(9):
        if board[i][col] == number:
            return False
    r = (row // 3) * 3
    c = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[r+i][c+j] == number:
                return False
    return True

def solve_cell():
    global board
    r, c = get_empty()
    if r is None:
        return True
    for i in range(1, 10):
        if is_valid(r, c, i):
            board[r][c] = i
            if solve_cell():
                return True
        board[r][c] = 0
    return False

def solve_board():
    global board
    solve_cell()
    return board

if __name__ == '__main__':
    board = get_board()
    row = len(board)
    col = len(board[0])
    if row != 9 or col != 9:
        raise Exception('Invalid rows and columns')
    print_board(board)
    solution = solve_board()
    print('Solution:')
    print_board(solution)
    write_board(solution)
