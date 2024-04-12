# Useful imports
import pyaoc
import math
import numpy as np
from functools import cache
from collections import defaultdict
import re

# Placeholders to be filled when copying the template
PART = 2
DAY = 19
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = 3

def find_all(rule, molecule):
    L = len(rule)
    for i in range(len(molecule) - L + 1):
        if rule == molecule[i:i+L]:
            yield (i, i + L)

def search(mol, rules, depth=0, seen: dict = defaultdict(lambda : np.inf)):
    if mol in seen:
        return seen[mol]
    
    print(mol)

    if mol == 'e':
        return depth
    
    best = np.inf
    for rule in rules:
        if rule[0] == 'e':
            if rule[1] == mol:
                return depth + 1
            continue
        
        for i, j in find_all(rule[1], mol):
            best = min(best, search(mol[:i] + rule[0] + mol[j:], rules, depth + 1, seen))

    seen[mol] = min(seen[mol], best)

    return best

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    
    rs, molecule = lines[:lines.index('')], lines[-1]

    rules = []
    for r in rs:
        a, b = r.split(" => ")
        rules.append((a, b, len(b) - len(a)))
    rules.sort(key=lambda x : x[2], reverse=True)

    return search(molecule, rules)

# Attempt to submit the current solve method
pyaoc.submit(
    solve, PART, DAY, YEAR, 
    test_result=TEST_RESULT,
    test=True
)