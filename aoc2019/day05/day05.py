#!/usr/bin/env python3
"""
Day 05 Advent of Code 2019. Additional functionality added from Day 02's
solution.
"""


class IntcodeComputer():
    """Main IntcodeComputer class
    :param program: List of ints that represent opcodes and inputs
    :type program: list
    """
    def __init__(self, program):
        self.og = program
        self.p = self.og.copy()
        self.cursor = 0
        self.ops_map = {
            1: lambda i, m, x: self.op1(i, i+1, i+2, m),
            2: lambda i, m, x: self.op2(i, i+1, i+2, m),
            3: lambda i, m, x: self.op3(x, i),
            4: lambda i, m, x: self.op4(i),
            5: lambda i, m, x: self.op5(i, i+1, m),
            6: lambda i, m, x: self.op6(i, i+1, m),
            7: lambda i, m, x: self.op7(i, i+1, i+2, m),
            8: lambda i, m, x: self.op8(i, i+1, i+2, m),
        }

    def op1(self, p1, p2, p3, pmodes):
        """Add the values at p1 and p2, store the result at p3"""
        p1mod, p2mod = pmodes
        self.p[self.p[p3]] = self.p_val(p1, p1mod) + self.p_val(p2, p2mod)
        self.cursor += 4

    def op2(self, p1, p2, p3, pmodes):
        """Multiply the values at p1 and p2, store the result at p3"""
        p1mod, p2mod = pmodes
        self.p[self.p[p3]] = self.p_val(p1, p1mod) * self.p_val(p2, p2mod)
        self.cursor += 4

    def op3(self, x, p1):
        """Set the value of the 'register' at p1 to the program's input value"""
        self.p[self.p[p1]] = x
        self.cursor += 2

    def op4(self, p1):
        """Output (print) the value stored at p1"""
        print(self.p[self.p[p1]], end=" ")
        self.cursor += 2

    def op5(self, p1, p2, pmodes):
        """If the value at p1 is non-zero, set the cursor to p2.
        Otherwise, do nothing.
        """
        p1mod, p2mod = pmodes
        if self.p_val(p1, p1mod) != 0:
            self.cursor = self.p_val(p2, p2mod)
        else:
            self.cursor += 3

    def op6(self, p1, p2, pmodes):
        """If the value at p1 equals zero, set the cursor to p2.
        Otherwise, do nothing.
        """
        p1mod, p2mod = pmodes
        if self.p_val(p1, p1mod) == 0:
            self.cursor = self.p_val(p2, p2mod)
        else:
            self.cursor += 3

    def op7(self, p1, p2, p3, pmodes):
        """p3 = (p1 > p2) ? 1 : 0"""
        p1mod, p2mod = pmodes
        lt = self.p_val(p1, p1mod) < self.p_val(p2, p2mod)
        self.p[self.p[p3]] = 1 if lt else 0
        self.cursor += 4

    def op8(self, p1, p2, p3, pmodes):
        """p3 = (p1 == p2) ? 1 : 0"""
        p1mod, p2mod = pmodes
        eq = self.p_val(p1, p1mod) == self.p_val(p2, p2mod)
        self.p[self.p[p3]] = 1 if eq else 0
        self.cursor += 4

    def parse_instr(self, inst):
        """For instructions with 'parameter modes':
        Return the opcode and a list of parameter modes to pass to `self.p_val`
        """
        if inst in [3, 4]:  # opcodes 3 & 4 do not need param modes
            return inst, None
        mod_bits, opcode = divmod(inst, 100)
        mod_bits, p1mod = divmod(mod_bits, 10)
        p2mod = divmod(mod_bits, 10)[1]
        param_modes = [p1mod, p2mod]

        return opcode, param_modes

    def p_val(self, pos, mode):
        """Return value based on parameter mode and index (position).
        0 ('position') mode 'dereferences' value stored at &pos
        1 ('immediate') mode uses immediate value of pos
        """
        if mode == 0:
            return self.p[self.p[pos]]
        elif mode == 1:
            return self.p[pos]

    def run(self, argx=None, show_program=False):
        """Run the int_code computer. Opcode '99' exits the program.
        :param show_program: Output the final program state after a successful run
        :type show_program: bool, defaults to False
        :param argx: Single input parameter given to the program (for opcode 3)
        :type argx: int, optional (for programs without opcode 3)
        """
        while self.p[self.cursor] != 99:
            op, modes = self.parse_instr(self.p[self.cursor])
            self.ops_map[op](self.cursor+1, modes, argx)
        if show_program:
            print(self.p)
        self.cursor = 0


if __name__ == '__main__':
    program = list(map(int, open('input.txt').read().strip('\n').split(',')))
    int_code = IntcodeComputer(program)
    int_code.run(argx=5)
