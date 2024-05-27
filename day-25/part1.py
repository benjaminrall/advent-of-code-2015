# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 1
DAY = 25
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = 16474243

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        line = f.readline().strip()[:-1]
    row, col = [x - 1 for x in map(int, line.split("row ")[1].split(", column "))]

    n = row + col
    code = col + n * (n + 1) // 2

    return (20151125 * pow(252533, code, 33554393)) % 33554393

if __name__ == "__main__":
	print(f"Test solution: {solve('test.txt')}")
	print(f"Actual solution: {solve('input.txt')}")
