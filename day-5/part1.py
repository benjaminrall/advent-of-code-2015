# Useful imports
import math
import numpy as np
from functools import cache

# Placeholders to be filled when copying the template
PART = 1
DAY = 5
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = 1

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    
    total = 0
    for line in lines:
        nice = True
        vowels = 0
        repeated = False
        for i, c in enumerate(line):
            if c in 'aeiou':
                vowels += 1
            if not repeated and i > 0:
                repeated = line[i] == line[i - 1]
        if vowels < 3 or not repeated:
            nice = False
            continue
        for invalid in ['ab', 'cd', 'pq', 'xy']:
            if invalid in line:
                nice = False
                break
        if nice:
            total += 1

    # --- SOLUTION CODE ---
    return total

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
