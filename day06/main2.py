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

def dir_char(dir):
    match dir:
        case (0, -1):
            return "^"
        case (1, 0):
            return ">"
        case (0, 1):
            return "v"
        case (-1, 0):
            return "<"

def over_limit(num, arr):
    return num < 0 or num >= len(arr)

def print_center(board, player, dir):
    area = 7
    for y_off in range(-(area // 2), area // 2 + 1):
        for x_off in range(-(area // 2), area // 2 + 1):
            if x_off == 0 and y_off== 0:
                print(dir_char(dir), end="")
            else:
                x = player[0] + x_off
                y = player[1] + y_off
                if over_limit(x, board[0]) or over_limit(y, board):
                    print("_", end="")
                else:
                    print("." if board[y][x] else "#", end="")
        print()
    print()

def print_path(path):
    for row in path:
        for tile in row:
            if len(tile) == 0:
                print(".", end="")
            elif len(tile) <= 2:
                if all(t == "v" or t == "^" for t in tile):
                    print("|", end="")
                elif all(t == "<" or t == ">" for t in tile):
                    print("-", end="")
            else:
                print("+", end="")

        print()
    print()

def path_finder(board, player):
    dir = (0, -1)
    path = [[set() for _ in row] for row in board]
    path[player[1]][player[0]].add(dir_char(dir))
    try:
        while True:
            np = move(player, dir)
            while not board[np[1]][np[0]]:
                dir = change_dir(dir)
                dc = dir_char(dir)
                if dc in path[player[1]][player[0]]:
                    return path, False
                else:
                    path[player[1]][player[0]].add(dc)
                np = move(player, dir)
            player = np
            dc = dir_char(dir)
            if dc in path[player[1]][player[0]]:
                return path, False
            else:
                path[player[1]][player[0]].add(dc)
            if player[0] < 0 or player[1] < 0:
                break
    except IndexError:
        pass
    return path, True

def deep_copy(board):
    return [list(row) for row in board]

board = [[tile != "#" for tile in row] for row in content.split("\n")]
line_len = content.index("\n")
player = content.index("^")
player = (player % (len(board[0]) + 1), player // (len(board[0]) + 1))

count = 0
original, finished = path_finder(board, player)
for y, row in enumerate(original):
    for x, tile in enumerate(row):
        if len(tile) == 0:
            continue
        if x == player[0] and y == player[1]:
            continue
        copy = deep_copy(board)
        copy[y][x] = False
        _, finished = path_finder(copy, player)
        if not finished:
            count += 1
    print(f"row {y} out of {len(original)} done")
print(count)
