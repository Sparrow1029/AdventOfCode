from collections import defaultdict

class Node(object):

    def __init__(self, val, direct_connections):
        self.ID = val
        self.direct_connections = direct_connections

class Web(object):

    def __init__(self):
        self.nodes = defaultdict()

    def add_new_node(self, node):
        self.nodes[node.ID] = node

    def find_num_nodes_connected_to_ID(self, node_id):
        count = 0
        for i in self.nodes[node_id].direct_connections:
            if i.ID == i:
                continue
            count += 1
            find_num_nodes_connected_to_ID(i)
        return count

#def connect_all_nodes(programs: dict):



programs = defaultdict(list)

f = open('input.txt', 'r')
inp = f.read().splitlines()
for line in inp:
    data = line.strip().split(' <-> ')
    programs[int(data[0])] = list(map(int, data[1].split(', ')))

# all_nodes = connect_all_nodes(programs)
# for k, v in all_nodes.items():
#     print(f'{k}: {v}')

web = Web()

for k,v in programs.items():
    node = Node(k, v)
    web.add_new_node(node)

for n in web.nodes:
    print(web.nodes[n].ID, web.nodes[n].direct_connections)
f.close()
