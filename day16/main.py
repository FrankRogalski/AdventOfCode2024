import numpy as np
import math

with open('test.txt') as file:
    content = file.read().strip()

grid = [
    [i for i in row]
    for row in content.split('\n')
]
s = content.index('S')
sx = s % (len(grid[0]) + 1)
sy = s // (len(grid[0]) + 1)
s = np.array([sy, sx])

e = content.index('E')
ex = e % (len(grid[0]) + 1)
ey = e // (len(grid[0]) + 1)
e = np.array([ey, ex])

dirs = np.array([
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1],
])

dir = 1

pos = s
path = [pos]

while True:
    p_steps = (dirs + pos).transpose()
    non_wall = np.argwhere(grid[*psteps] != '#')
    diff = np.abs(non_wall - dirs[dir]) #TODO fix, we need to find the indecies of the non walls in the original dirs
    rotations = numpy.minimum(diff, 4 - diff)
    cost = rotations * 1000 + (non_wall - e)
