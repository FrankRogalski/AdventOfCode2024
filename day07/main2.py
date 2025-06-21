from operator import mul, add
from itertools import product
from math import log10, floor

with open("input.txt") as file:
    content = file.read().strip()

def concat(a, b):
    return a * 10 ** (floor(log10(b)) + 1) + b

total = 0
lines = content.split("\n")
for line_num, line in enumerate(lines):
    solution, part_string = line.split(": ")
    solution = int(solution)
    parts = [int(i) for i in part_string.split(" ")]
    for combination in product((mul, add, concat), repeat=len(parts) - 1):
        res = parts[0]
        for op, part in zip(combination, parts[1:]):
            res = op(res, part)
        if res == solution:
            total += res
            break
    print(f"line {line_num} out of {len(lines)} complete")
print(total)
