# Useful imports
import math
import numpy as np
from functools import cache

# Placeholders to be filled when copying the template
PART = 1
DAY = 1
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = -1

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        return sum([1 if c == '(' else -1 for c in f.read().strip()])

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
