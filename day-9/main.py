# Useful imports
import pyaoc
import math
import numpy as np
from functools import cache
from collections import defaultdict
from scipy.sparse.csgraph import minimum_spanning_tree

# Placeholders to be filled when copying the template
PART = 1
DAY = 9
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = 605

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    locations = defaultdict(lambda : len(locations))
    distances = []

    for line in lines:
        loc1, _, loc2, _, d = line.split(" ")
        distances.append((locations[loc1], locations[loc2], d))
    
    matrix = np.zeros((len(locations), len(locations)))
    for i, j, k in distances:
        matrix[i, j] = k
        matrix[j, i] = k    

    # --- SOLUTION CODE ---
    return None

# Attempt to submit the current solve method
pyaoc.submit(
    solve, PART, DAY, YEAR, 
    test_result=TEST_RESULT,
    test=True
)