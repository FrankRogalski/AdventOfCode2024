import numpy as np
from collections import namedtuple as nt

Values = nt('Values', ['size', 'read', 'file'])
v = Values(7, 12, 'test.txt')
#v = Values(70, 1024, 'input.txt')

with open(v.file) as file:
    content = file.read().strip()

blocks = np.array([
    [int(i) for i in row.split(',')][::-1]
    for row in content.split('\n')[:v.read]
]).transpose()

grid = np.zeros((v.size, v.size), dtype=int)
grid[*blocks] = 1

print(grid)
