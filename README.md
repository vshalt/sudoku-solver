# Sudoku Solver

- Solve sudoku puzzles with backtracking algorithm

## Sections
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)

### Introduction
Sudoku is a 9x9 puzzle. The basic rules of sudoku are to arrange numbers from 1-9 in such a way that:
- No number repeats in a row
- No number repeats in a column
- No number repeats in the 3x3 square that it belongs to

If the above conditions are met, we say that the puzzle is solved.

### Installation
You can install the project locally by cloning the repo
`git clone https://github.com/vshalt/sudoku-solver`

### Usage
- Open the `input.txt` file.
- Input your puzzle in the following format, replace empty slots by `0`.
```
3 7 1 6 5 0 0 9 0
0 0 9 2 0 0 0 8 7
0 4 2 0 0 9 5 0 0
0 0 0 0 8 0 7 0 3
0 0 0 4 0 5 0 0 0
4 0 7 0 9 0 0 0 0
0 0 3 9 0 0 1 5 0
9 1 0 0 0 3 6 0 0
0 6 0 0 1 4 2 3 9
```
- After your puzzle is written in `input.txt`, run the program by typing `python3 solver.py`.
- The solution will be printed in the terminal. Also a copy will be saved in a new file called `solution.txt`
