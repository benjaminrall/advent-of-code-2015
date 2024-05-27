# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 1
DAY = 24
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = 99

def search(packages, remaining, output: list[list], path: list = []):
    if sum(packages) < remaining:
        return False
    
    if remaining < 0:
        return False
    
    if remaining == 0:
        output[0].append([x for x in path])
        return True
    
    for i, package in enumerate(packages):
        if package <= remaining:
            path.append(package)
            search(packages[i + 1:], remaining - package, output, path)
            path.pop()
            
# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f: 
        packages = sorted([int(line.strip()) for line in f.readlines()], reverse=True)

    size = sum(packages) // 3

    output = [[]]
    search(packages, size, output)
    combinations = output[0]

    best = (None, np.inf, np.inf)
    for c in combinations:
        if len(c) < best[1]:
            p = 1
            for x in c:
                p *= x
            best = (c, len(c), p)
        elif len(c) == best[1]:
            p = 1
            for x in c:
                p *= x 
            if p < best[2]:
                best = (c, len(c), p)

    return best[2]

if __name__ == "__main__":
	print(f"Test solution: {solve('test.txt')}")
	print(f"Actual solution: {solve('input.txt')}")
