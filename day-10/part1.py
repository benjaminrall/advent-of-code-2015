# Useful imports
import math
import numpy as np
from functools import cache

# Placeholders to be filled when copying the template
PART = 1
DAY = 10
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = None

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    
    sequence = lines[0]

    ITERATIONS = 40
    for i in range(ITERATIONS):
        current = sequence[0]
        count = 1
        new = ""
        for letter in sequence[1:]:
            if current != letter:
                new += f"{count}{current}"
                count = 1
                current = letter
            else:
                count += 1
        new += f"{count}{sequence[-1]}"
        sequence = new

    return len(sequence)

if __name__ == "__main__":	
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
