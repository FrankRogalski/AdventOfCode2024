from operator import mul, add

with open("input.txt") as file:
    content = file.read().strip()

total = 0
lines = content.split("\n")
for line_num, line in enumerate(lines):
    solution, part_string = line.split(": ")
    solution = int(solution)
    parts = [int(i) for i in part_string.split(" ")]
    gaps = len(parts) - 1
    for combination in range(2**gaps):
        res = 0
        for i in range(gaps):
            if (combination >> i) & 1 == 1:
                op = add
            else:
                op = mul

            if i == 0:
                res = op(parts[0], parts[1])
            else:
                res = op(res, parts[i + 1])
        if res == solution:
            total += res
            break
    print(f"line {line_num} out of {len(lines)} complete")
print(total)
