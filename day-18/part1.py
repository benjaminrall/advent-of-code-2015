# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict
from scipy.signal import convolve2d

# Placeholders to be filled when copying the template
PART = 1
DAY = 18
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = 4

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    
    grid = np.array([[1 if c == '#' else 0 for c in line] for line in lines])

    STEPS = 100
    g = np.zeros(grid.shape, dtype=int)
    for step in range(STEPS):
        k = convolve2d(grid, np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]]), mode="same")
        g[:, :] = -1
        g[k == 2] = 0
        g[k == 3] = 1
        grid = np.clip(grid + g, 0, 1)

    return np.sum(grid)

if __name__ == "__main__":
	print(f"Test solution: {solve('test.txt')}")
	print(f"Actual solution: {solve('input.txt')}")
