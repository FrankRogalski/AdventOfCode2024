with open('input.txt') as file:
    content = file.read().strip()

grid = [
    [i for i in row]
    for row in content.split('\n')
]

dirs = ((0, -1), (1, 0), (0, 1), (-1, 0))

def flood_fill(grid, x, y, used):
    used.add((x, y))
    tile = grid[y][x] 
    for dx, dy in dirs:
        nx = x + dx
        ny = y + dy
        if (nx >= 0 and nx < len(grid[0])
            and ny >= 0 and ny < len(grid)
            and grid[ny][nx] == tile
            and (nx, ny) not in used):
            flood_fill(grid, nx, ny, used)

def add(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

def sub(t1, t2):
    return (t1[0] - t2[0], t1[1] - t2[1])

def edge_calculator(used):
    sides = 0
    for x, y in used:
        start = (x, y)
        break
    dir = 0
    while start in used:
        start = add(start, dirs[dir])
    start = sub(start, dirs[dir])
    current = start
    dir = (dir + 1) % len(dirs)
    start_dir = dir
    first = True

    while current != start or start_dir != dir or first == True:
        first = False
        dir = (dir - 1) % len(dirs)
        current = add(current, dirs[dir])
        if current in used:
            sides += 1
            continue

        current = sub(current, dirs[dir])
        dir = (dir + 1) % len(dirs)
        current = add(current, dirs[dir])
        if current in used:
            continue

        current = sub(current, dirs[dir])
        dir = (dir + 1) % len(dirs)
        sides += 1
        
    return sides


regions = []
used_global = set()

total = 0
for y, row in enumerate(grid):
    for x, space in enumerate(row):
        if (x, y) in used_global:
            continue
        used = set()
        flood_fill(grid, x, y, used)
        regions.append(used)
        used_global.update(used)
        edges = edge_calculator(used)
        total += edges * len(used)
print(total)

