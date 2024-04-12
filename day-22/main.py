# Useful imports
import pyaoc
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 2
DAY = 22
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = 212

SPELLS = [
    [53, 0],
    [73, 1],
    [113, 2],
    [173, 3],
    [229, 4],
]

def search(health, mana, spent, boss, attack, best=[np.inf], turn=1, effects=[], depth=0):
    if turn:
        health -= 1
        if health <= 0:
            return

    df = 0
    new_effects = []
    active = set()
    for effect in effects:
        t, d = effect

        # Handles effects
        if t == 0:
            df = 7
        elif t == 1:
            boss -= 3
            if boss <= 0:
                best[0] = min(best[0], spent)
                return
        elif t == 2:
            mana += 101
        d -= 1

        # Handles expiring effects
        if d != 0:
            new_effects.append((t, d))
            active.add(t + 2)

    effects = new_effects
    
    # Boss' turn
    if not turn:
        dmg = attack - df
        if health - dmg <= 0:
            return
        search(health - dmg, mana, spent, boss, attack, best, 1, effects, depth + 1)
        return
    
    # Player turn
    for cost, spell in [s for s in SPELLS if s[0] <= mana and s[1] not in active]:

        new_mana = mana - cost
        new_spent = spent + cost

        if new_spent >= best[0]:
            return False

        if spell == 0:
            if boss - 4 <= 0:
                best[0] = min(best[0], new_spent)
            else:
                search(health, new_mana, new_spent, boss - 4, attack, best, 0, effects, depth + 1)
        elif spell == 1:
            if boss - 2 <= 0:
                best[0] = min(best[0], new_spent)
            else:
                search(health + 2, new_mana, new_spent, boss - 2, attack, best, 0, effects, depth + 1)
        elif spell == 2:
            search(health, new_mana, new_spent, boss, attack, best, 0, effects + [(0, 6)], depth + 1)
        elif spell == 3:
            search(health, new_mana, new_spent, boss, attack, best, 0, effects + [(1, 6)], depth + 1)
        elif spell == 4:
            search(health, new_mana, new_spent, boss, attack, best, 0, effects + [(2, 5)], depth + 1)

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [int(line.strip().split(": ")[1]) for line in f.readlines()]
    
    boss = np.array(lines)

    best = [np.inf]

    search(50, 500, 0, boss[0], boss[1], best)

    return best[0]

# Attempt to submit the current solve method
pyaoc.submit(
    solve, PART, DAY, YEAR, 
    test_result=TEST_RESULT,
    test=True
)