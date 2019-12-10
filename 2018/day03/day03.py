#!/usr/bin/env python3

from collections import namedtuple
from pprint import pprint
from time import sleep

Rectangle = namedtuple('Rectangle', 'id_ xmin ymin xmax ymax')


def rect_from_data(input_str) -> Rectangle:
    """Return Rectangle object from input lines"""
    data = input_str.split()

    id_ = int(data[0].lstrip('#'))
    dimensions = tuple(map(int, data[3].split('x')))
    xmin, ymin = map(int, data[2].rstrip(':').split(','))
    xmax, ymax = xmin + dimensions[0], ymin + dimensions[1]

    return Rectangle(id_, xmin, ymin, xmax, ymax)


def parse_input_data(inp_file) -> list:
    """Parse input file from AoC"""

    rectangles = []
    with open(inp_file) as fh:
        for line in fh.read().splitlines():
            rectangles.append(rect_from_data(line))

    return rectangles


def get_intersect(r1: Rectangle, r2: Rectangle):
    """Determine if Rectangles overlap. If they do,
        return the resulting Rectangle."""

    max_mins = (max(r1.xmin, r2.xmin), max(r1.ymin, r2.ymin))
    min_maxs = (min(r1.xmax, r2.xmax), min(r1.ymax, r2.ymax))
    test = Rectangle(r1.id_, *max_mins, *min_maxs)

    if (r1.xmax >= test.xmin >= r1.xmin) and (r1.ymax >= test.ymin >= r1.ymin):
        intersect = test
        return intersect

    return None


def get_covered_squares(rect: Rectangle) -> set:
    """Return a set of grid squares covered by found intersecting rectangles"""

    # +1 to each coordinate to map to grid squares instead of vertices
    xs, ys = range(rect.xmin+1, rect.xmax+1), range(rect.ymin+1, rect.ymax+1)
    return set((x, y) for x in xs for y in ys)


if __name__ == '__main__':
    covered = set()

    rectangles = parse_input_data('input.txt')
    overlap_ids = set(rect.id_ for rect in rectangles)

    for i in range(len(rectangles)-1):
        r1 = rectangles[i]
        for r2 in rectangles[i+1:]:
            intersect = get_intersect(r1, r2)
            if intersect:
                overlap = get_covered_squares(intersect)
                if not len(overlap):
                    continue
                covered.update(overlap)
                try:
                    overlap_ids.remove(r1.id_)
                    overlap_ids.remove(r2.id_)
                except KeyError:
                    pass
            elif intersect is None:
                continue

    second_pass = [rect for rect in rectangles if rect.id_ in overlap_ids]

    for i in range(len(second_pass)-1):
        ra = second_pass[i]
        for rb in second_pass[i+1:]:
            print(f"ra: {ra.id_}   rb: {rb.id_}")
            intersect = get_intersect(ra, rb)
            if intersect:
                overlap = get_covered_squares(intersect)
                print(overlap)

    print(len(covered))
    pprint(overlap_ids, compact=True)
