# Useful imports
import pyaoc
import math
import numpy as np
from functools import cache

# Placeholders to be filled when copying the template
PART = 1
DAY = 7
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = 0

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    
    calculations = {}
    values = {}
    for line in lines:
        c, s = line.split(' -> ')
        c = c.split(" ")
        if len(c) == 0:
            calculations[s] = (0, int(c[0]))
        elif len(c) == 1:
            calculations[s] = (1, c[1])
        elif c[1] == 'AND':
            calculations[s] = (2, c[0], c[2])
        elif c[1] == 'OR':
            calculations[s] = (3, c[0], c[2])
        elif c[1] == 'LSHIFT':
            calculations[s] = (4, c[0], int(c[2]))
        elif c[1] == 'RSHIFT':
            calculations[s] = (5, c[0], int(c[2]))

    stack = ['a']
    value = 0
    while len(stack) > 0:
        if stack[-1] in values:
            value = values[stack.pop()]
            continue
        


    # --- SOLUTION CODE ---
    return None

# Attempt to submit the current solve method
pyaoc.submit(
    solve, PART, DAY, YEAR, 
    test_result=TEST_RESULT,
    test=True
)