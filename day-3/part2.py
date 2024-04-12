# Useful imports
import math
import numpy as np
from functools import cache

# Placeholders to be filled when copying the template
PART = 2
DAY = 3
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = 3

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

    pos1 = complex(0, 0)
    pos2 = complex(0, 0)
    visited = set([pos1])
    for i, char in enumerate(line):
        if i % 2 == 0:
            pos1 += DIRS[char]
            visited.add(pos1)
        else:
            pos2 += DIRS[char]
            visited.add(pos2)

    return len(visited)

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
