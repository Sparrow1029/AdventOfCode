#!/usr/bin/env python3
from collections import defaultdict

with open('input.txt', 'r') as f:
    data = f.read().splitlines()
    orbit_data = defaultdict(list)
    planets = set()
    for i in data:
        planet, orbited_by = i.split(')')
        orbit_data[planet].append(orbited_by)
        planets.update([planet, orbited_by])


def find_path(graph, start, end, path=[]):
    """Recursively search through 'graph' nodes for path to specified end node"""
    path = path + [start]
    if start == end:
        return path
    if start not in graph.keys():
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None


# Part 1
total = sum(len(find_path(orbit_data, 'COM', p)) for p in planets) - len(planets)
# Had to subtract 1 from each list to account for the planet itself  ^^^
print(f"Part 1\n-------\ntotal indirect + direct orbits: {total}")

# Part 2
# Find the point where the paths to YOU and SAN bifurcate with set logic
path_to_SAN = set(find_path(orbit_data, 'COM', 'SAN'))
path_to_YOU = set(find_path(orbit_data, 'COM', 'YOU'))
total2 = len(path_to_SAN ^ path_to_YOU) - 2  # <-- remove 'SAN' & 'YOU'
print(f"\nPart 2\n-------\ntotal orbital jumps from you to santa: {total2}")
