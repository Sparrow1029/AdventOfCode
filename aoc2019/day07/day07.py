from itertools import permutations
from intcode import Amplifier

data = open('input.txt', 'r').read().split(',')
program = list(map(int, data))


def max_thruster_signal(program, rng):
    max_output = 0

    for seq in permutations(rng):
        ampA = Amplifier('A', seq[0], program)
        ampB = Amplifier('B', seq[1], program)
        ampC = Amplifier('C', seq[2], program)
        ampD = Amplifier('D', seq[3], program)
        ampE = Amplifier('E', seq[4], program)

        ampA.connect(ampB)
        ampB.connect(ampC)
        ampC.connect(ampD)
        ampD.connect(ampE)
        ampE.connect(ampA)

        ampA.recv(0)
        ampA.run()

        if ampE.output > max_output:
            max_output = ampE.output

    return max_output


# Part 1
print(max_thruster_signal(program, range(5)))

# Part 2
print(max_thruster_signal(program, range(5, 10)))
