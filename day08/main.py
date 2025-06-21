from itertools import permutations

with open('input.txt') as file:
    content = file.read().strip()

def bounds(idx, arr):
    return idx >= 0 and idx < len(arr)

rows = content.split('\n')
row_len = len(rows[0])

locations = dict()
for y, row in enumerate():
    for x, chr in enumerate(row):
        if chr != '.':
            if chr not in locations:
                locations[chr] = []
            locations[chr].append((x, y))

total = 0
for positions in locations:
    for a, b in permutations(positions, 2):
        xd = a[0] - b[0]
        yd = a[1] - b[1]

        x = a[0] - xd
        y = a[1] - xy
        if bounds(x, row_len) and bounds(y, len(rows)):
            total += 1

        x = b[0] + xd
        y = b[1] + xy
        if bounds(x, row_len) and bounds(y, len(rows)):
            total += 1
print(total)           
