# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict
from itertools import combinations

# Placeholders to be filled when copying the template
PART = 1
DAY = 21
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = 0

WEAPONS = np.array([
    [0, 4, 0, 8],
    [0, 5, 0, 10],
    [0, 6, 0, 25],
    [0, 7, 0, 40],
    [0, 8, 0, 74],
])

ARMOURS = np.array([
    [0, 0, 1, 13],
    [0, 0, 2, 31],
    [0, 0, 3, 53],
    [0, 0, 4, 75],
    [0, 0, 5, 102]
])

RINGS = np.array([
    [0, 1, 0, 25],
    [0, 2, 0, 50],
    [0, 3, 0, 100],
    [0, 0, 1, 20],
    [0, 0, 2, 40],
    [0, 0, 3, 80],
])

RING_COMBOS = [np.array([0, 0, 0, 0])] + [c[0] for c in combinations(RINGS, 1)] + [c[0] + c[1] for c in combinations(RINGS, 2)]

def battle(player, boss) -> bool:
    player_dmg = max(1, player[1] - boss[2])
    boss_dmg = max(1, boss[1] - player[2])

    player_rounds = int(np.ceil(player[0] / boss_dmg))
    boss_rounds = int(np.ceil(boss[0] / player_dmg))

    return player_rounds >= boss_rounds

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [int(line.strip().split(": ")[1]) for line in f.readlines()]
    
    boss = np.array(lines)
    player = np.array([100, 0, 0, 0])

    costs = []
    for weapon in WEAPONS:
        for armour in ARMOURS:
            for rings in RING_COMBOS:
                p = player + weapon + armour + rings
                if battle(p, boss):
                    costs.append(p[-1])

    return min(costs)

if __name__ == "__main__":
	print(f"Test solution: {solve('test.txt')}")
	print(f"Actual solution: {solve('input.txt')}")
