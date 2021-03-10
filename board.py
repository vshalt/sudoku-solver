import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(BASE_DIR, 'input.txt')

def get_board():
    with open(path, 'r') as file:
        arr = file.read()
        arr = arr.split()
    if len(arr) != 81:
        raise IOError('Invalid board, check again')
    grid = []
    for i in range(9):
        grid.append(arr[9*i: 9*i+9])
    return grid

def write_board(grid):
    arr = []
    for i in range(9):
        arr.append(' '.join(grid[i]))

    with open(path, 'a') as file:
        file.write('\nSolution:\n')
        file.write('\n'.join(arr))

