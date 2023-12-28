# Useful imports
import math
import numpy as np
from functools import cache

# Placeholders to be filled when copying the template
PART = 2
DAY = 2
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = 34

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        lines = [sorted([int(c) for c in line.strip().split('x')]) for line in f.readlines()]
    
    total = 0
    for line in lines:
        total += 2 * (line[0] + line[1]) + np.prod(line)
    # --- SOLUTION CODE ---
    return total

print(f"Test solution: {solve('test.txt')}")
print(f"Actual solution: {solve('input.txt')}")
