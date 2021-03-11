import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
read_path = os.path.join(BASE_DIR, 'input.txt')
write_path = os.path.join(BASE_DIR, 'solution.txt')

def get_board():
    with open(read_path, 'r') as file:
        arr = file.read()
        arr = arr.split()
    if len(arr) != 81:
        raise IOError('Invalid board, check again')
    grid = []
    temp = []
    for i in range(9):
        for j in range(9):
            temp.append(int(arr[9*i + j]))
        grid.append(temp)
        temp = []
    return grid

def write_board(grid):
    arr = []
    for i in range(9):
        arr.append(' '.join(str(j) for j in grid[i]))

    with open(write_path, 'w') as file:
        file.write('Solution:\n')
        file.write('\n'.join(arr))

