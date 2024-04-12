# Useful imports
import math
import numpy as np
from functools import cache
import json

# Placeholders to be filled when copying the template
PART = 1
DAY = 12
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = 6

def count(obj) -> int:
    if type(obj) == int:
        return obj
    
    if type(obj) == dict:
        total = 0
        for key in obj:
            total += count(obj[key])
        return total
    
    if type(obj) == list:
        total = 0
        for element in obj:
            total += count(element)
        return total

    return 0

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    obj = json.loads(lines[0])

    return count(obj)

if __name__ == "__main__":	
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
