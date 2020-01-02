#!/usr/bin/env python3
import sys
from collections import namedtuple

Point = namedtuple('Point', 'x y')


def slope(a, b):
    return (a.y - b.y) / (a.x - b.x)


def intercept(pt, slope):
    return pt.y - slope * pt.x


def pt_is_on_line(pt, m, b):
    return pt.y == m * pt.x + b


def in_bounds(point):
    return (0 <= point.x <= 20) and (0 <= point.y <= 20)


def create_graph(inp_file):
    with open(inp_file, 'r') as f:
        data = f.readlines()

    graph = []
    for y, line in enumerate(data):
        row = []
        for x in range(len(line)):
            if line[x] == '#':
                row.append(Point(x, -y))
        graph.append(row)

    return graph


def get_quadrants(graph, a):
    q1 = [pt for pt in graph if pt.x < a.x and pt.y > a.y] if a.x > 0 else None
    q2 = [pt for pt in graph if pt.x > a.x and pt.y > a.y] if a.x < 19 else None
    q3 = [pt for pt in graph if pt.x < a.x and pt.y < a.y] if a.y < 0 else None
    q4 = [pt for pt in graph if pt.x > a.x and pt.y > a.y] if a.y > -19 else None

    return q1, q2, q3, q4


def get_compass(graph, ast, all_asteroids):
    field = all_asteroids.copy()
    field.remove(ast)
    x, y = ast.x, ast.y
    n = min([pt for pt in field if pt.x == x])
    e = min([pt for pt in field if pt.y == y])
    s = max([pt for pt in field if pt.x == x])
    w = max([pt for pt in field if pt.y == y])
    ne, se, sw, nw = [None]*4
    cur_x, cur_y = x+1, y+1
    while in_bounds(cur_x, cur_y):
        if (cur_x, cur_y) in field:
            pass

    return [a for a in (n, e, s, w) if a is not None]


if __name__ == '__main__':
    assert len(sys.argv) == 2

    graph = create_graph(sys.argv[1])
    all_asteroids = graph[0]
    for i in graph[1:]:
        all_asteroids.extend(i)

    print(all_asteroids[18])
    quads = get_quadrants(all_asteroids, all_asteroids[18])
    i = 1
    for q in quads:
        if q:
            print(f"Quad {i}")
            for p in q:
                print(f"({p.x}, {p.y})")
        i += 1
    print(get_NESW(all_asteroids, all_asteroids[18]))
