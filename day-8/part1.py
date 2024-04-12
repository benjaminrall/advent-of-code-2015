# Useful imports
import math
import numpy as np
from functools import cache

# Placeholders to be filled when copying the template
PART = 1
DAY = 8
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = 12

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    total = 0
    for line in lines:
        edited = line[1:-1].replace('\\\\', ' ').replace('\\"', '"')
        hex_count = edited.count('\\x')
        string_length = len(edited) - 3 * hex_count
        total += len(line) - string_length

    return total

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
