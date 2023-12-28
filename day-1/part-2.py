# Useful imports
import math
import numpy as np
from functools import cache

# Placeholders to be filled when copying the template
PART = 2
DAY = 1
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = 5

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        line = f.read().strip()

    counter = 0
    for i, c in enumerate(line):
        if c == '(':
            counter += 1
        else:
            counter -= 1
        if counter == -1:
            return i + 1

print(f"Test solution: {solve('test.txt')}")
print(f"Actual solution: {solve('input.txt')}")
