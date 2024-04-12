# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 2
DAY = 13
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = 286

def search(person, table, graph, d = 0, i = 0, visited: set = set()):
    if len(table) == len(visited) + 1:
        return d + graph[person][table[0]]

    best = -np.inf

    visited.add(person)
    for name, value in [(key, graph[person][key]) for key in graph[person] if key not in visited]:
        table[i] = person
        best = max(best, search(name, table, graph, d + value, i + 1, visited))
    table[i] = None
    visited.remove(person)

    return best

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        lines = [line.strip()[:-1].split() for line in f.readlines()]
    
    graph = defaultdict(lambda : defaultdict(lambda : 0))
    for line in lines:
        value = (1 if line[2] == 'gain' else -1) * int(line[3])
        graph[line[0]][line[-1]] += value
        graph[line[-1]][line[0]] += value

    for person in [key for key in graph]:
        graph[person]['Me'] = 0
        graph['Me'][person] = 0

    table = [None for _ in range(len(graph))]
    
    return search('Alice', table, graph)

if __name__ == "__main__":
	print(f"Test solution: {solve('test.txt')}")
	print(f"Actual solution: {solve('input.txt')}")
