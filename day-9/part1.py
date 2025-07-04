# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 1
DAY = 9
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = 605

def search(node: str, graph: dict, dist: int = 0, visited: set = set()) -> int:
    if len(graph) == len(visited) + 1:
        return dist
    
    visited.add(node)

    best = np.inf

    for loc, d in [(loc, graph[node][loc]) for loc in graph[node] if loc not in visited]:
        best = min(best, search(loc, graph, dist + d, visited))

    visited.remove(node)

    return best


# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    graph = defaultdict(lambda : {})

    for line in lines:
        loc1, _, loc2, _, d = line.split(" ")
        graph[loc1][loc2] = int(d)
        graph[loc2][loc1] = int(d)
        
    return min([search(loc, graph) for loc in graph])

if __name__ == "__main__":	
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
