# Useful imports
import math
import numpy as np
from functools import cache
from collections import Counter

# Placeholders to be filled when copying the template
PART = 2
DAY = 5
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = 2

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    
    total = 0
    for line in lines:
        pairs = []
        i = 0
        while i < len(line) - 1:
            if line[i] == line[i + 1]:
                pairs.append(line[i] + line[i])
                if i < len(line) - 2 and line[i] == line[i + 2]:
                    i += 1
            else:
                pairs.append(line[i] + line[i + 1])
            i += 1
        count = Counter(pairs)
        if count.most_common(1)[0][1] < 2:
            continue
        for i in range(len(line) - 2):
            if line[i] == line[i + 2]:
                total += 1
                break

    return total

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
