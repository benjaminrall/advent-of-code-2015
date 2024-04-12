# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 1
DAY = 16
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = 0

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        lines = [line.strip().split() for line in f.readlines()]
    sues = []
    for line in lines:
        sue = {}
        for i in range(2, len(line), 2):
            sue[line[i].replace(":", "")] =  int(line[i + 1].replace(",", ""))
        sues.append(sue)

    TARGET = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }

    for i in range(500):
        sue = sues[i]
        found = True
        for key in sue:
            if sue[key] != TARGET[key]:
                found = False
                break
        if found:
            return i + 1

    return None

if __name__ == "__main__":
	print(f"Test solution: {solve('test.txt')}")
	print(f"Actual solution: {solve('input.txt')}")
