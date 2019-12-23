#!/usr/bin/env python3
from collections import Counter, defaultdict
from pprint import pprint as pp

with open('input.txt', 'r') as f:
    data = f.read().splitlines()
    orbit_data = defaultdict(list)
    for i in data:
        planet, orbited_by = i.split(')')
        orbit_data[planet].append(orbited_by)

num_direct_orbits = sum(len(v) for v in orbit_data.values())
print(num_direct_orbits)

pp(orbit_data, compact=True)

cnt = 0
cur_planet = 'COM'


def recurse_dict(data, cur):
    global cnt
    global cur_planet

    try:
        cnt += 1
        if len(data[cur]) > 1:
            print(f"\nNEW ROOT {cur}")
            print(f"          / \\")
            print(f"       {orbit_data[cur]}")
            cur_planet = cur
        for i in data[cur]:
            print(f"{i} --> ", end='')
            recurse_dict(data, i)
    except KeyError: 
        print(f"Current Planet: {cur_planet}, {data[cur_planet]}")
        return recurse_dict(cur_planet)


recurse_dict(orbit_data, 'COM')
print(cnt)


class Node():
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

    def __iter__(self):
        return iter(self.children)

    def __repr__(self):
        if self.children:
            print(f"{self.name}")

# root = Node('COM')
# print(orbit_data['COM'][0])
# root.children.append(Node(orbit_data['COM'][0], parent=root))
# print(root)
