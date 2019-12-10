#!/usr/bin/env python3


def recursive_mass(mass):
    if mass <= 0:
        return 0
    else:
        return mass + recursive_mass(mass//3-2)


with open('input.txt') as fh:
    data = list(map(int, fh.read().splitlines()))
    # part 1
    fuel = list(map(lambda x: (x//3)-2, data))
    print(sum(fuel))
    # part 2
    print(sum(map(lambda x: recursive_mass(x), fuel)))
