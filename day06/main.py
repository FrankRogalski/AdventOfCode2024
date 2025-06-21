with open("input.txt") as file:
    content = file.read().strip()

def change_dir(dir):
    match dir:
        case (0, -1):
            return (1, 0)
        case (1, 0):
            return (0, 1)
        case (0, 1):
            return (-1, 0)
        case (-1, 0):
            return (0, -1)

def move(player, dir):
    return (player[0] + dir[0], player[1] + dir[1])

def over_limit(num, arr):
    return num < 0 or num >= len(arr)

board = [[tile != "#" for tile in row] for row in content.split("\n")]
line_len = content.index("\n")
player = content.index("^")
player = (player % (len(board[0]) + 1), player // (len(board[0]) + 1))
dir = (0, -1)
unique = set()
unique.add(player)
try:
    while True:
        np = move(player, dir)
        while not board[np[1]][np[0]]:
            dir = change_dir(dir)
            np = move(player, dir)
        player = np
        if player[0] < 0 or player[1] < 0:
            raise IndexError("Python!!!!")
        unique.add(player)
except IndexError:
    print(len(unique))
