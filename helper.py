def print_board(grid):
    horizontal_sep = (('+'+ ('-'*7))*3) + '+'
    print(horizontal_sep)
    for i in range(9):
        for j in range(9):
            if j %3 == 0:
                print('| ', end="")
            number = grid[i][j]
            if number == 0:
                print('_ ', end="")
            else:
                print(f'{number} ', end="")
            if j == 8:
                print('| ', end="")
        print()
        if (i+1)%3 == 0:
            print(horizontal_sep)
