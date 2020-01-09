#!/usr/bin/env python3
"""
Day 09 Advent of Code 2019. Additional functionality added from Day 07's
solution.
"""


def parse_file(input_file):
    path = ('./' + input_file)
    with open(path, 'r') as f:
        data = f.read().strip().split(',')
        return list(map(int, data))


class IntcodeComputer():
    """Main IntcodeComputer class """

    def __init__(self, program):
        self.orig = program
        self.p = program.copy()
        # Extend memory
        self.p.extend([0] * 65536)
        self.cursor = 0
        self.rel_base = 0
        self.out = []
        self.ops_map = {
            1: lambda i, m, x: self.op1(i, i+1, i+2, m),
            2: lambda i, m, x: self.op2(i, i+1, i+2, m),
            3: lambda i, m, x: self.op3(x, i, m),
            4: lambda i, m, x: self.op4(i, m),
            5: lambda i, m, x: self.op5(i, i+1, m),
            6: lambda i, m, x: self.op6(i, i+1, m),
            7: lambda i, m, x: self.op7(i, i+1, i+2, m),
            8: lambda i, m, x: self.op8(i, i+1, i+2, m),
            9: lambda i, m, x: self.op9(i, m)
        }

    def op1(self, p1, p2, p3, pmodes):
        """Add the values at p1 and p2, store the result at p3"""
        p1mod, p2mod, p3mod = pmodes
        self.p[self.p_val(p3, p3mod, 'w')] = self.p_val(p1, p1mod) + self.p_val(p2, p2mod)
        self.cursor += 4

    def op2(self, p1, p2, p3, pmodes):
        """Multiply the values at p1 and p2, store the result at p3"""
        p1mod, p2mod, p3mod = pmodes
        self.p[self.p_val(p3, p3mod, 'w')] = self.p_val(p1, p1mod) * self.p_val(p2, p2mod)
        self.cursor += 4

    def op3(self, x, p1, pmodes):
        """Set the value of the 'register' at p1 to the program's input value"""
        p1mod, p2mod, p3mod = pmodes
        self.p[self.p_val(p1, p1mod, 'w')] = x
        self.cursor += 2

    def op4(self, p1, pmodes):
        """Output (print) the value stored at p1"""
        p1mod, p2mod, p3mod = pmodes
        self.out.append(self.p_val(p1, p1mod, 'r'))
        self.cursor += 2

    def op5(self, p1, p2, pmodes):
        """If the value at p1 is non-zero, set the cursor to p2.
        Otherwise, do nothing.
        """
        p1mod, p2mod, p3mod = pmodes
        if self.p_val(p1, p1mod) != 0:
            self.cursor = self.p_val(p2, p2mod)
        else:
            self.cursor += 3

    def op6(self, p1, p2, pmodes):
        """If the value at p1 equals zero, set the cursor to p2.
        Otherwise, do nothing.
        """
        p1mod, p2mod, p3mod = pmodes
        if self.p_val(p1, p1mod) == 0:
            self.cursor = self.p_val(p2, p2mod)
        else:
            self.cursor += 3

    def op7(self, p1, p2, p3, pmodes):
        """p3 = (p1 > p2) ? 1 : 0"""
        p1mod, p2mod, p3mod = pmodes
        lt = self.p_val(p1, p1mod) < self.p_val(p2, p2mod)
        self.p[self.p_val(p3, p3mod, 'w')] = 1 if lt else 0
        self.cursor += 4

    def op8(self, p1, p2, p3, pmodes):
        """p3 = (p1 == p2) ? 1 : 0"""
        p1mod, p2mod, p3mod = pmodes
        eq = self.p_val(p1, p1mod) == self.p_val(p2, p2mod)
        self.p[self.p_val(p3, p3mod, 'w')] = 1 if eq else 0
        self.cursor += 4

    def op9(self, p1, pmodes):
        p1mod, p2mod, p3mod = pmodes
        self.rel_base += self.p_val(p1, p1mod)
        self.cursor += 2


    def parse_instr(self, inst):
        """For instructions with 'parameter modes':
        Return the opcode and a list of parameter modes to pass to `self.p_val`
        """
        mod_bits, opcode = divmod(inst, 100)
        mod_bits, p1mod = divmod(mod_bits, 10)
        mod_bits, p2mod = divmod(mod_bits, 10)
        p3mod = divmod(mod_bits, 10)[1]
        param_modes = [p1mod, p2mod, p3mod]

        return opcode, param_modes

    def p_val(self, pos, mode, tx='r'):
        """Return value based on parameter mode and index (position).
        0 ('position') mode 'dereferences' value stored at &pos
        1 ('immediate') mode uses immediate value of pos
        2 ('relative') mode like 0 but + rel_base
        """
        if tx == 'r':
            if mode == 0:
                return self.p[self.p[pos]]
            if mode == 1:
                return self.p[pos]
            if mode == 2:
                return self.p[self.p[pos] + self.rel_base]
        if tx == 'w':
            if mode in [0, 1]:
                return self.p[pos]
            if mode == 2:
                return self.p[pos] + self.rel_base

    def run(self, argx=None, output=True):
        """Run the int_code computer. Opcode '99' exits the program."""
        while self.p[self.cursor] != 99:
            op, modes = self.parse_instr(self.p[self.cursor])
            self.ops_map[op](self.cursor+1, modes, argx)
        if output:
            print(self.out)

    def reset(self):
        self.__init__(self.orig)
