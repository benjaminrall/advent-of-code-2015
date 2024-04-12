# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 1
DAY = 14
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = 0

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        lines = [line.strip().split() for line in f.readlines()]

    reindeer = []
    for line in lines:
        reindeer.append((int(line[3]), int(line[6]), int(line[-2])))

    best = -np.inf
    TARGET = 2503
    for speed, move, rest in reindeer:
        tx, ty = TARGET // (move + rest), min(TARGET % (move + rest), move)
        best = max(best, speed * (move * tx + ty))

    return best

if __name__ == "__main__":
	print(f"Test solution: {solve('test.txt')}")
	print(f"Actual solution: {solve('input.txt')}")
