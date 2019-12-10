from collections import defaultdict
import networkx as nx

graph = nx.Graph()

f = open('input.txt', 'r')
inp = f.read().splitlines()

for line in inp:
    node, neighbors = line.split(' <-> ')
    graph.add_edges_from((node, neighbor) for neighbor in neighbors.split(', '))

print("Part 1:", len(nx.node_connected_component(graph, '0')))
print("Part 2:", nx.number_connected_components(graph))
