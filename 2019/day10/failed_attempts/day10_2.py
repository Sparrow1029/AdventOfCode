#!/usr/bin/env python3
import sys
from pprint import pprint
from operator import itemgetter
from collections import namedtuple, defaultdict

Point = namedtuple('Point', 'x y')


def slope(a, b):
    return (a.y - b.y) / (a.x - b.x)


def intercept(pt, slope):
    return pt.y - slope * pt.x


def in_bounds(point, w, h):
    return (0 <= point.x < w) and (0 <= point.y < h)


def create_graph(inp_file):
    with open(inp_file, 'r') as f:
        data = f.read().splitlines()

    graph = []
    width = len(data[0])
    height = len(data)
    for y, line in enumerate(data):
        row = []
        for x in range(len(line)):
            if line[x] == '#':
                row.append(Point(x, y))
        graph.extend(row)

    return graph, width, height


def get_nesw(graph, visible, asteroid):
    x, y = asteroid.x, asteroid.y
    N = [pt for pt in graph if pt.x == x and pt.y > y]
    E = [pt for pt in graph if pt.y == y and pt.x > x]
    S = [pt for pt in graph if pt.x == x and pt.y < y]
    W = [pt for pt in graph if pt.y == y and pt.x < x]
    n = min(N) if N else None
    e = min(E) if E else None
    s = max(S) if S else None
    w = max(W) if W else None

    print(f"N: {n}  E:{e}  S: {s}  W: {w}")
    visible.update(set([d for d in (n, e, s, w) if d is not None]))
    graph.difference_update(set(N + E + S + W))


def get_visible(graph, visible, asteroid):
    while len(graph):
        remaining = graph.pop()
        print(f"Testing {remaining}")
        m = slope(asteroid, remaining)
        b = intercept(asteroid, m)
        print(f"slope {m}  intercept {b}")
        x1, x2 = min(remaining.x, asteroid.x), max(remaining.x, asteroid.x)
        rng = range(x1+1, x2)
        print(f"rng = {list(rng)}")
        test_points = []
        for x in rng:
            y = m*float(x) + b
            print(Point(x, y))
            if y.is_integer():
                test_pt = Point(x, int(y))
                if test_pt in graph:
                    print(f"Point between points: test_pt")
                    test_points.append(Point(x, int(y)))
        if test_points:
            print(f"TEST POINTS: {test_points}")
            visible.add(min(test_points))
            graph.difference_update(test_points)
            pprint(f"AFTER CHECK: vis {visible}  graph {graph}", compact=True)
        else:
            visible.add(remaining)
            pprint(f"No points between adding r to visible\n{visible}", compact=True)


if __name__ == '__main__':
    assert len(sys.argv) == 2
    graph, W, H = create_graph(sys.argv[1])
    seen_data = dict()
    for asteroid in sorted(graph):
        print(asteroid)
        test_graph = set(graph.copy())
        test_graph.remove(asteroid)
        visible = set()

        get_nesw(test_graph, visible, asteroid)
        get_visible(test_graph, visible, asteroid)

        seen_data[asteroid] = len(visible)
        print('\n\n')

    pprint(seen_data)
    print(max(seen_data.items(), key=itemgetter(1))[0])
