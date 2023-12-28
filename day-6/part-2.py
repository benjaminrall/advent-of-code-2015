# Useful imports
import math
import numpy as np
from functools import cache

# Placeholders to be filled when copying the template
PART = 2
DAY = 6
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = None

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        lines = [line.strip().split(' ') for line in f.readlines()]
    
    grid = np.zeros((1000, 1000), dtype=int)

    for line in lines:
        through = line.index('through')
        start = [int(c) for c in line[through - 1].split(',')]
        end = [int(c) + 1 for c in line[through + 1].split(',')]
        instruction = line[through - 2]
        if instruction == 'on':
            grid[start[0]:end[0], start[1]:end[1]] += 1
        elif instruction == 'off':
            grid[start[0]:end[0], start[1]:end[1]] = np.where(grid[start[0]:end[0], start[1]:end[1]] > 0, grid[start[0]:end[0], start[1]:end[1]] - 1, 0)
        else:
            grid[start[0]:end[0], start[1]:end[1]] += 2


    # --- SOLUTION CODE ---
    return grid.sum()

print(f"Test solution: {solve('test.txt')}")
print(f"Actual solution: {solve('input.txt')}")
