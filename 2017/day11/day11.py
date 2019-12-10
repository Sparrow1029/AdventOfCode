DIRECTION = ['n', 'ne', 'se', 's', 'sw', 'nw']
POINTS = [(0, 1), (1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1)]

NEIGHBORS = dict(zip(DIRECTION, POINTS))

START = (0, 0)

def find_child_pos(directions, start):
    cur_pos = start
    farthest_dist = 0  # part 2

    for direction in directions:
        x1, y1 = cur_pos
        x2, y2 = NEIGHBORS[direction]
        new_pos = (x1+x2, y1+y2)

        # Part 2
        if hex_mnhtn_dist(start, new_pos) > farthest_dist:
            farthest_dist = hex_mnhtn_dist(start, new_pos)

        cur_pos = new_pos

    return cur_pos, farthest_dist

def hex_mnhtn_dist(pt1, pt2):
    x0, y0 = pt1
    x1, y1 = pt2

    dx = x1 - x0
    dy = y1 - y0

    sign_dx = bool(dx > 0)
    sign_dy = bool(dy > 0)

    if sign_dx == sign_dy:
        return abs(dx + dy)
    else:
        return max(abs(dx), abs(dy))

inp = open('input.txt', 'r').read().strip().split(',')

child_pos, farthest_dist = find_child_pos(inp, START)
print(hex_mnhtn_dist(START, child_pos))
print(farthest_dist)
