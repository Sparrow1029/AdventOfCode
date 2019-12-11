#!/usr/bin/env python3
"""
Advent of Code 2019 - Day 3 in Python
"""


def parse_input(input_file) -> list:
    with open(input_file) as f:
        raw = f.read().splitlines()  # gets two wires
        wire1 = raw[0].split(',')
        wire2 = raw[1].split(',')
    return [wire1, wire2]


def convert_instructions(input_data) -> list:
    """Convert list of wire moves to coordinate tuples using a dict map
    of lambda functions.
    """
    map_to_tup = {
        'R': lambda m: (int(m), 0),
        'D': lambda m: (0, -int(m)),
        'L': lambda m: (-int(m), 0),
        'U': lambda m: (0, int(m))
    }

    wire1 = input_data[0]
    wire2 = input_data[1]
    wire1_instructions = []
    wire2_instructions = []

    for i in wire1:
        wire1_instructions.append(map_to_tup[i[0]](i[1:]))
    for i in wire2:
        wire2_instructions.append(map_to_tup[i[0]](i[1:]))

    return [wire1_instructions, wire2_instructions]


def get_new_pos(prev_pos, move) -> tuple:
    return (prev_pos[0]+move[0], prev_pos[1]+move[1])


def get_line_coords(point1, point2) -> list:
    """Return a list of all coordinates on the line between points 1 and 2"""
    x1, y1, x2, y2 = *point1, *point2
    if x1 == x2:  # vertical line
        if y2 < y1:
            return [(x1, y) for y in range(y1, y2, -1)]
        else:
            return [(x1, y) for y in range(y1, y2)]
    elif y1 == y2:  # horizontal line
        if x2 < x1:
            return [(x, y1) for x in range(x1, x2, -1)]
        else:
            return [(x, y1) for x in range(x1, x2)]


def get_all_wire_coords(moves, origin=(0, 0)) -> set:
    """Return a set of all unique coordinates the wire passes over"""
    wire_coords = []
    prev_pos = origin
    while moves:
        move = moves.pop(0)
        cur_pos = get_new_pos(prev_pos, move)
        new_line_coords = get_line_coords(prev_pos, cur_pos)
        wire_coords.extend(new_line_coords)
        prev_pos = cur_pos

    return set(wire_coords)


def num_steps_to_ixs(wire_moves, intersections: set):
    """Count the total steps taken by the wire. If the current position
    is an intersection of the two wires, record current steps and coord in a list.
    """
    steps = 0
    steps_ixs = []
    prev_pos = (0, 0)
    while wire_moves:
        move = wire_moves.pop(0)
        cur_pos = get_new_pos(prev_pos, move)
        new_line_coords = get_line_coords(prev_pos, cur_pos)
        for c in new_line_coords:
            if c in intersections:
                steps_ixs.append((steps, c))
            steps += 1
        prev_pos = cur_pos

    return steps_ixs


def manhattan_distance(point2, point1=(0, 0)):
    x1, y1, x2, y2 = *point1, *point2
    return abs(x1 - x2) + abs(y1 - y2)


if __name__ == '__main__':
    input_data = parse_input('input.txt')
    wires = convert_instructions(input_data)

    # Part 1
    wire1 = get_all_wire_coords(wires[0].copy())
    wire2 = get_all_wire_coords(wires[1].copy())
    intersections = wire1.intersection(wire2)
    intersections.remove((0, 0))  # origin (0, 0) doesn't count for purposes of puzzle

    print(min(map(lambda p: manhattan_distance(p), intersections)))

    # Part 2
    w1 = num_steps_to_ixs(wires[0], intersections)
    w2 = num_steps_to_ixs(wires[1], intersections)
    combined_steps = []
    for steps, ix in w1:
        for steps2, ix2 in w2:
            if ix == ix2:
                combined_steps.append(steps + steps2)

    print(min(combined_steps))
