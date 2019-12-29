#!/usr/bin/env python3

from intcode import IntcodeComputer
# from alex_intcode import IntcodeComputer

with open('input.txt', 'r') as f:
    data = f.read().split(',')
    program = list(map(int, data))

computer = IntcodeComputer(program)
# Part 1
computer.run(argx=1)

# Part 2
computer.reset()
computer.run(argx=2)
