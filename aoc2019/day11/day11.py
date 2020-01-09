#!/usr/bin/env python3
from collections import defaultdict
from pprint import pprint
import sys
sys.path.append("..")

from day09.intcode import IntcodeComputer, parse_file


class PaintBot():
    def __init__(self, program):
        self.cpu = IntcodeComputer(program)
        self.instr_q = self.cpu.out
        self.grid = defaultdict(list)
        self.cur_pos = [0, 0]
        self.cur_facing = '^'  # up
        self.colors = {
            0: ' ',
            1: '█'
        }
        self.turns = {
            '^': ['<', '>'],
            '>': ['^', 'v'],
            'v': ['>', '<'],
            '<': ['v', '^']
        }
        self.moves = {
            '^': lambda pos: [pos[0], pos[1]+1],
            '>': lambda pos: [pos[0]+1, pos[1]],
            'v': lambda pos: [pos[0], pos[1]-1],
            '<': lambda pos: [pos[0]-1, pos[1]]
        }

    def load_instr(self, output=True):
        self.cpu.run(argx=0, output=output)

    def run(self):
        facings = [self.cur_facing]
        positions = [self.cur_pos]
        while self.instr_q:
            color = self.instr_q.pop(0)
            instr = self.instr_q.pop(0)
            self.exe(instr, color)
            facings.append(self.cur_facing)
            positions.append(self.cur_pos)
        # print(facings)
        # print(positions)

    def exe(self, instr, color_code):
        paint = self.colors[color_code]
        cur_xy = (self.cur_pos[0], self.cur_pos[1])
        if cur_xy in self.grid:
            self.grid[cur_xy][0] = paint  # color
            self.grid[cur_xy][1] += 1     # num times visited
        else:
            self.grid[cur_xy] = [paint, 1]

        new_facing = self.turns[self.cur_facing][instr]
        new_pos = self.moves[self.cur_facing](self.cur_pos)

        self.cur_facing = new_facing
        self.cur_pos = new_pos

    def show(self, q=False, grid=True):
        if q:
            print(self.instr_q)
        if grid:
            pprint(self.grid)


program = parse_file('input.txt')

p = PaintBot(program)
p.load_instr(output=False)
p.run()
# p.show()
