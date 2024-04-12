# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 1
DAY = 23
YEAR = 2015

# The expected result from the test input, if using a test input
TEST_RESULT = 0

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    
    registers = {'a': 0, 'b': 0}
    instructions = {}
    for i, line in enumerate(lines):
        spl = line.index(" ")
        opcode, operands = line[:spl], line[spl+1:].split(", ")
        instructions[i] = (opcode, operands)
    
    pc = 0
    while pc >= 0 and pc < len(instructions):
        opcode, operands = instructions[pc]

        if opcode == 'hlf':
            registers[operands[0]] //= 2
            pc += 1
        elif opcode == 'tpl':
            registers[operands[0]] *= 3
            pc += 1
        elif opcode == 'inc':
            registers[operands[0]] += 1
            pc += 1
        elif opcode == 'jmp':
            pc += int(operands[0])
        elif opcode == 'jie':
            pc += int(operands[1]) if registers[operands[0]] % 2 == 0 else 1
        elif opcode == 'jio':
            pc += int(operands[1]) if registers[operands[0]] == 1 else 1

    return registers['b']

if __name__ == "__main__":
	print(f"Test solution: {solve('test.txt')}")
	print(f"Actual solution: {solve('input.txt')}")
