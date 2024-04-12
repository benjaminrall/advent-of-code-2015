# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 1
DAY = 15
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = 62842880

def search(ingredients, choices = [], total=100, i=0):
    if i + 1 == len(ingredients):
        choices += [100 - sum(choices)]
        return np.prod(np.maximum(np.sum([ingredient * c for ingredient, c in zip(ingredients, choices)], axis=0), 0))
    
    best = -np.inf
    for n in range(total + 1):
        best = max(best, search(ingredients, choices + [n], total - n, i + 1))

    return best


# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        lines = [line.strip().replace(",", "").split() for line in f.readlines()]

    ingredients = []
    for line in lines:
        ingredients.append(np.array((int(line[2]), int(line[4]), int(line[6]), int(line[8]))))

    return search(ingredients)

if __name__ == "__main__":
	print(f"Test solution: {solve('test.txt')}")
	print(f"Actual solution: {solve('input.txt')}")
