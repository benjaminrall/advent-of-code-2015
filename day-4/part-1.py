# Useful imports
import math
import numpy as np
from functools import cache
import hashlib

# Placeholders to be filled when copying the template
PART = 1
DAY = 4
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = 1048970

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        word = f.read().strip()

    i = 1
    while True:
        result = hashlib.md5((word + str(i)).encode())
        if result.hexdigest().startswith("00000"):
            return i 
        i += 1

print(f"Test solution: {solve('test.txt')}")
print(f"Actual solution: {solve('input.txt')}")
