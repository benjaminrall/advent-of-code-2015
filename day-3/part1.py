# Useful imports
import math
import numpy as np
from functools import cache

# Placeholders to be filled when copying the template
PART = 1
DAY = 3
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = 4

DIRS = {
    '^': complex(-1, 0),
    'v': complex(1, 0),
    '>': complex(0, 1),
    '<': complex(0, -1)
}

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        line = f.read().strip()

    pos = complex(0, 0)
    visited = set([pos])
    for char in line:
        pos += DIRS[char]
        visited.add(pos)

    # --- SOLUTION CODE ---
    return len(visited)

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
