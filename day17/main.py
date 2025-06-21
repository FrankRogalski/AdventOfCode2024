import re

with open('input.txt') as file:
    content = file.read().strip()

registers, program = content.split('\n\n')

registers = list(map(int, re.sub(r'Register \w: ', '', registers).split('\n')))
program = list(map(int, program.split(' ')[1].split(',')))

def combo(index):
    if index <= 3:
        return index
    else:
        return registers[index - 4]

def compute(instruction, literal):
    match instruction:
        case 0:
            registers[0] = registers[0] // 2 ** combo(literal)
        case 1:
            registers[1] = registers[1] ^ literal
        case 2:
            registers[1] = combo(literal) % 8
        case 3:
            if registers[0] != 0:
                return literal
        case 4:
            registers[1] = registers[1] ^ registers[2]
        case 5:
            print(combo(literal) % 8, end=',')
        case 6:
            registers[1] = registers[0] // 2 ** combo(literal)
        case 7:
            registers[2] = registers[0] // 2 ** combo(literal)
    return -1
                

i = 0
while i >= 0 and i < len(program) - 1:
    if (res := compute(program[i], program[i + 1])) != -1:
        i = res
        continue
    i += 2

