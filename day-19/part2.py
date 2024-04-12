# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict
import random

# Placeholders to be filled when copying the template
PART = 2
DAY = 19
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = 3

def find_all(rule, molecule):
    L = len(rule)
    for i in range(len(molecule) - L,  -1, -1):
        if rule == molecule[i:i+L]:
            yield (i, i + L)

def search(mol, rules, depth=0, seen: dict = defaultdict(lambda : np.inf)):
    if mol in seen:
        return seen[mol]
    
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
        rules.append((a, b))
    
    total = 0

    target = molecule
    while target != "e":
        temp = target
        for a, b in rules:
            if b not in target:
                continue

            target = target.replace(b, a, 1)
            total += 1
        
        if temp == target:
            target = molecule
            total = 0
            random.shuffle(rules)

    return total

if __name__ == "__main__":
	print(f"Test solution: {solve('test.txt')}")
	print(f"Actual solution: {solve('input.txt')}")
