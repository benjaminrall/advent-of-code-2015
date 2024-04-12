# Useful imports
import math
import numpy as np
from functools import cache

# Placeholders to be filled when copying the template
PART = 1
DAY = 11
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = "ghjaabcc"

class Base26:
    size = 8
    blacklist = [ord(c) - ord('a') for c in 'iol']

    def __init__(self, num: list[int]) -> None:
        self.num = num

    @staticmethod
    def from_string(string: str) -> 'Base26':
        return Base26([int(ord(c) - ord('a')) for c in string])
    
    def increment(self, i: int = -1):
        if i < 0:
            i += self.size
        
        for j in range(i + 1, self.size):
            self.num[j] = 0

        res = self.num[i] + 1        
        self.num[i] = res % 26
        if res // 26:
            self.increment(i - 1)

    def __str__(self) -> str:
        return ''.join([chr(ord('a') + d) for d in self.num])
    
    def valid(self) -> bool:
        # Rule 2
        for i in range(self.size - 1, -1, -1):
            if self.num[i] in self.blacklist:
                self.increment(i)
                return False

        # Rule 1
        found = False
        for i in range(2, self.size):
            a = self.num[i]
            b = self.num[i - 1]
            c = self.num[i - 2]
            if a == b + 1 and a == c + 2:
                found = True
                break

        if not found:
            return False
            
        # Rule 3
        i = 0
        count = 0
        while i < self.size - 1:
            if self.num[i] == self.num[i + 1]:
                count += 1
                i += 1
            i += 1

        return count >= 2
                


# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- INPUT HANDLING ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    string_password = lines[0]

    password = Base26.from_string(string_password)

    while not password.valid():
        password.increment()

    return str(password)


if __name__ == "__main__":	
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
