#!/usr/bin/env python3
"""
This is nearly completely stolen from reddit here:
https://www.reddit.com/r/adventofcode/comments/e8m1z3/2019_day_10_solutions/favdnox

u/fazmad used atan2 to calculate the angle from each asteroid to every other asteroid.
Part 1: set logic prevents the same angle from being counted twice, simulating that
only ONE asteroid on a given tangent line will be visible

Part 2: order all the asteroids by their angle and then manhattan distance --
    angle starts at zero (12 o'clock), and manhattan distance closest to origin
    Vaporize until you get to the 200th asteroid.
"""
import sys
import math
from pprint import pprint
from operator import itemgetter
from collections import namedtuple

Point = namedtuple('Point', 'x y')


def create_graph(inp_file):
    with open(inp_file, 'r') as f:
        data = f.read().splitlines()

    graph = []
    for y, line in enumerate(data):
        row = []
        for x in range(len(line)):
            if line[x] == '#':
                row.append(Point(x, y))
        graph.extend(row)

    return graph


def angle(astrd, test):
    result = math.atan2(test.x - astrd.x, astrd.y - test.y) * 180 / math.pi
    if result < 0:
        return 360 + result
    return result


def main():
    assert len(sys.argv) == 2
    asteroids = create_graph(sys.argv[1])
    seen_data = dict()
    for a in asteroids:
        seen_data[a] = len(set(angle(a, test) for test in asteroids if a != test))

    best = max(seen_data.items(), key=itemgetter(1))[0]
    # Part 1
    print(best, seen_data[best])

    # Part 2
    asteroids.remove(best)
    angles = sorted(
        ((angle(best, end), end) for end in asteroids),
        key=lambda p: (p[0], abs(best.x - p[1].x) + abs(best.y - p[1].y))
    )
    # pprint(angles)

    idx = 0
    last = angles.pop(idx)
    last_angle = last[0]
    cnt = 1

    while cnt < 200 and angles:
        if idx >= len(angles):
            idx = 0
            last_angle = None
        if last_angle == angles[idx][0]:
            idx += 1
            continue
        # print(f'vaporized {last}')
        last = angles.pop(idx)
        last_angle = last[0]
        cnt += 1
    print(f"vaporized {cnt, last[1], last[1].x * 100 + last[1].y}")


if __name__ == '__main__':
    main()
