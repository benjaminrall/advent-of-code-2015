# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict
import re

# Placeholders to be filled when copying the template
PART = 1
DAY = 19
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = 4

def find_all(rule, molecule):
    L = len(rule)
    for i in range(len(molecule) - L + 1):
        if rule == molecule[i:i+L]:
            yield (i, i + L)

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    
    rs, molecule = lines[:lines.index('')], lines[-1]

    rules = defaultdict(lambda : [])
    for r in rs:
        a, b = r.split(" => ")
        rules[a].append(b)

    replacements = set()
    for rule in rules:
        for i, j in find_all(rule, molecule):
            for r in rules[rule]:
                replacements.add(molecule[:i] + r + molecule[j:])

    return len(replacements)

if __name__ == "__main__":
	print(f"Test solution: {solve('test.txt')}")
	print(f"Actual solution: {solve('input.txt')}")
