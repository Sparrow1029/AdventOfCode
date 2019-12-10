#!/usr/bin/env python3
from itertools import combinations_with_replacement

program = list(map(int, open('input.txt').read().strip('\n').split(',')))


def intcode(opcode: int, index: int, program: list):
    # return_index = index + 4
    param1 = program[program[index+1]] 
    param2 = program[program[index+2]]
    param3 = program[index+3]
    if opcode == 1:
        val = param1 + param2
    elif opcode == 2:
        val = param1 * param2
    program[param3] = val


# Part 1
programPart1 = program.copy()
programPart1[1] = 12
programPart1[2] = 2

try:
    for pos in range(0, len(program), 4):
        if programPart1[pos] == 99:
            break
        intcode(programPart1[pos], pos, programPart1)
except IndexError:
    pass

print(programPart1)


# Part 2
def gen_values():
    nums = list(range(100)) + list(range(99, 0, -1))
    yield from combinations_with_replacement(nums, 2)


combo = gen_values()
while True:
    programPart2 = program.copy()
    noun, verb = next(combo)
    programPart2[1] = noun
    programPart2[2] = verb
    try:
        for pos in range(0, len(programPart2), 4):
            if programPart2[pos] == 99:
                break
            intcode(programPart2[pos], pos, programPart2)
    except IndexError:
        continue
    if programPart2[0] == 19690720:
        print(f"Found: ({noun}, {verb}) = 19690720")
        print(100 * noun + verb)
        break
