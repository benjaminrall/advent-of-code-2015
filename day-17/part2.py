# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 2
DAY = 17
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = 0

def search(containers, amount, outcomes, i=0, used=[]):
    if amount == 0:
        outcomes.append(used)
        return 1
    if amount < 0:
        return 0
    if sum(containers[i:]) < amount:
        return 0
    
    total = 0
    for j in range(i, len(containers)):
        c = containers[j]
        total += search(containers, amount - c, outcomes, j + 1, used + [c])

    return total

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        containers = sorted([int(line.strip()) for line in f.readlines()], reverse=True)
    
    LITRES = 150
    outcomes = []

    search(containers, LITRES, outcomes)

    if len(outcomes) == 0:
        return 0
    
    min_length = sorted([len(o) for o in outcomes])[0]
    
    return len([o for o in outcomes if len(o) == min_length])

if __name__ == "__main__":
	print(f"Test solution: {solve('test.txt')}")
	print(f"Actual solution: {solve('input.txt')}")
