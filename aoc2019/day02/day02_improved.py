#!/usr/bin/env python3
from itertools import combinations_with_replacement

program = list(map(int, open('input.txt').read().strip('\n').split(',')))


class IntcodeComputer():
    def __init__(self, program):
        self.p = program
        self.cursor = 0
        self.ops_dict = {
            1: lambda i: self.op1(i, i+1, i+2),
            2: lambda i: self.op2(i, i+1, i+2),
            3: lambda i: self.op3(i, i+1),
            4: lambda i: self.op4(i)
        }

    def op1(self, p1, p2, p3):
        self.p[self.p[p3]] = self.p[self.p[p1]] + self.p[self.p[p2]]
        self.cursor += 4

    def op2(self, p1, p2, p3):
        self.p[self.p[p3]] = self.p[self.p[p1]] * self.p[self.p[p2]]
        self.cursor += 4

    def op3(self, p1, p2):
        self.p[p1] = self.p[self.p[p2]]
        self.cursor += 3

    def op4(self, p1):
        print(self.p[self.p[p1]])
        self.cursor += 2
        return self.p[self.p[p1]]

    def run(self):
        while self.p[self.cursor] != 99:
            self.ops_dict[self.p[self.cursor]](self.cursor+1)
        print(self.p)

int_code = IntcodeComputer([3,0,4,0,99])
