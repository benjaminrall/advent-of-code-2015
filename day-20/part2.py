# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 2
DAY = 20
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = 8

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    target = int(np.ceil(int(lines[0]) / 11))

    levels = defaultdict(lambda : 0)
    for i in range(1, target + 1):
        for j in range(50):
            levels[i * (j + 1)] += i
        if levels[i] >= target:
            return i
        
    return None

if __name__ == "__main__":
	print(f"Test solution: {solve('test.txt')}")
	print(f"Actual solution: {solve('input.txt')}")
