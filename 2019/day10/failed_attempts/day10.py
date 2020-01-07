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


def get_visible_rows(graph, visible, ast):
    rows = set([a for a in graph if a.y in [ast.y+1, ast.y-1]])
    cols = set([a for a in graph if a.x in [ast.x+1, ast.x-1]])
    visible.update(rows.union(cols))
    graph.difference_update(visible)

    # return rows.union(cols)


def get_nesw(graph, visible, asteroid):
    x, y = asteroid.x, asteroid.y
    N = [pt for pt in graph if pt.x == x and pt.y > y]
    E = [pt for pt in graph if pt.y == y and pt.x > x]
    S = [pt for pt in graph if pt.x == x and pt.y < y]
    W = [pt for pt in graph if pt.y == y and pt.x < x]
    n = min(N, key=lambda p: p.y) if N else None
    e = min(E) if E else None
    s = max(S) if S else None
    w = max(W) if W else None

    print(f"N: {n}  E:{e}  S: {s}  W: {w}")
    visible.update(set([d for d in (n, e, s, w) if d is not None]))
    graph.difference_update(set(N + E + S + W))


def get_diag(graph, visible, asteroid, w, h):
    directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    all_diag = []
    for d in directions:
        fnd = False
        mov_x, mov_y = d
        cur_x, cur_y = asteroid.x, asteroid.y
        pt = asteroid
        # while in_bounds(pt, w, h):
        while True:
            cur_x += mov_x
            cur_y += mov_y
            pt = Point(cur_x, cur_y)
            if not in_bounds(pt, w, h):
                break
            all_diag.append(pt)
            if pt in graph:
                if not fnd:
                    fnd = True
                    print(f"DIRECT DIAG {pt}")
                    visible.add(pt)
                graph.remove(pt)
        fnd = False
        cur_x, cur_y = asteroid.x, asteroid.y
    print(f"All DIAG {sorted(all_diag)}")


def get_remaining(graph, visible, asteroid):
    while len(graph):
        remaining = graph.pop()
        print(f"REMAIN {remaining}")
        m = slope(asteroid, remaining)
        b = intercept(asteroid, m)
        print(f"chk {remaining}  slope {m}")
        x1, x2 = min(remaining.x, asteroid.x), max(remaining.x, asteroid.x)
        rng = range(x1+1, x2)
        print(list(rng))
        test_points = []
        for x in rng:
            y = m*float(x) + b
            if y.is_integer():
                test_pt = Point(x, int(y))
                if test_pt in graph:
                    test_points.append(test_pt)
        if len(test_points):
            print("TEST POINTS")
            print(test_points)
            print(f"MIN {min(test_points)}")
            visible.add(min(test_points))
            graph.difference_update(test_points)
        else:
            visible.add(remaining)


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
        get_diag(test_graph, visible, asteroid, W, H)
        get_visible_rows(test_graph, visible, asteroid)
        # visible.update(get_visible_rows(test_graph, asteroid))
        # test_graph.difference_update(visible)
        get_remaining(test_graph, visible, asteroid)

        seen_data[asteroid] = len(visible)
        print('\n\n')

    pprint(seen_data)
    print(max(seen_data.items(), key=itemgetter(1))[0])

    print(W, H)
