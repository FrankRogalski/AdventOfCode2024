import math

with open('input.txt') as file:
    content = file.read().strip().split(' ')

numbers = [int(i) for i in content]

def digits(num):
    return int(math.log10(num)) + 1

for round in range(25):
    for i in range(len(numbers) - 1, -1, -1):
        if numbers[i] == 0:
            numbers[i] = 1
        else:
            exponent, even = divmod(digits(numbers[i]), 2)
            if even == 0:
                split = 10 ** exponent
                first, second = divmod(numbers[i], split)
                numbers.insert(i + 1, second)
                numbers[i] = first
            else:
                numbers[i] *= 2024
    print(round)
print(len(numbers))
