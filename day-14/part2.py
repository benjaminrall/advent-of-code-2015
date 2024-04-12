# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 2
DAY = 14
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = 689

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        lines = [line.strip().split() for line in f.readlines()]

    reindeer = []
    for line in lines:
        reindeer.append((int(line[3]), int(line[6]), int(line[-2])))

    TARGET = 2503
    scores = np.zeros(len(reindeer), dtype=int)
    distances = np.zeros(len(reindeer), dtype=int)
    for second in range(1, TARGET + 1):
        for i, (speed, move, rest) in enumerate(reindeer):
            tx, ty = second // (move + rest), min(second % (move + rest), move)
            distances[i] = speed * (move * tx + ty)
        scores += (distances == np.max(distances)).astype(int)

    return np.max(scores)

if __name__ == "__main__":
	print(f"Test solution: {solve('test.txt')}")
	print(f"Actual solution: {solve('input.txt')}")
