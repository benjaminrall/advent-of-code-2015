# Useful imports
import pyaoc
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 1
DAY = 24
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = 88

def prod(bin, limit=np.inf):
    total = 1
    for v in bin:
        total *= v
        if total >= limit:
            return limit
    return total

def search(packages, bins: list[list], size: int, best: list):
    if len(packages) == 0:
        best[0] = prod(bins[0], best[0])
        print(bins)
        return
    
    if prod(bins[0], best[0]) >= best[0]:
        return

    package = packages[0]
    packages = packages[1:]
    for bin in bins:
        if package + sum(bin) <= size:
            bin.append(package)
            search(packages, bins, size, best)
            bin.remove(package)

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        packages = sorted([int(line.strip()) for line in f.readlines()], reverse=True)
    
    bin_size = int(np.ceil(sum(packages) / 3))
    bins = [[] for _ in range(3)]
    
    best = [np.inf]

    search(packages, bins, bin_size, best)

    return best[0]

# Attempt to submit the current solve method
pyaoc.submit(
    solve, PART, DAY, YEAR, 
    test_result=TEST_RESULT,
    test=True
)