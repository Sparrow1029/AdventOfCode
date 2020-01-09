#!/usr/bin/env python3
if __name__ == '__main__':
    from intcode import IntcodeComputer, parse_file

    program = parse_file('input.txt')

    computer = IntcodeComputer(program)
    # Part 1
    computer.run(argx=1)

    # Part 2
    computer.reset()
    computer.run(argx=2)
