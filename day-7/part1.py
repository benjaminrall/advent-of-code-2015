# Useful imports
import math
import numpy as np
from functools import cache

# Placeholders to be filled when copying the template
PART = 1
DAY = 7
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = 65079

def calculate(character, calculations, values):    
    if character in values:
        return values[character]
    try:
        return np.array([character], dtype=np.uint16)
    except:
        pass
    
    calculation = calculations[character]
    v = None
    match calculation[0]:
        case 0:
            v = calculate(calculation[1], calculations, values)
        case 1:
            v = ~calculate(calculation[1], calculations, values)
        case 2:
            v = calculate(calculation[1], calculations, values) & calculate(calculation[2], calculations, values)
        case 3:
            v = calculate(calculation[1], calculations, values) | calculate(calculation[2], calculations, values)
        case 4:
            v = calculate(calculation[1], calculations, values) << calculate(calculation[2], calculations, values)
        case 5:
            v = calculate(calculation[1], calculations, values) >> calculate(calculation[2], calculations, values)
    values[character] = v
    return v
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
        if len(c) == 1:
            try:
                values[s] = np.array([c[0]], dtype=np.uint16)
            except:
                calculations[s] = (0, c[0])
        elif len(c) == 2:
            calculations[s] = (1, c[1])
        elif c[1] == 'AND':
            calculations[s] = (2, c[0], c[2])
        elif c[1] == 'OR':
            calculations[s] = (3, c[0], c[2])
        elif c[1] == 'LSHIFT':
            calculations[s] = (4, c[0], c[2])
        elif c[1] == 'RSHIFT':
            calculations[s] = (5, c[0], c[2])

    # --- SOLUTION CODE ---
    return calculate('a', calculations, values)[0]

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
