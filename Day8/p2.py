import itertools as it
from math import gcd


with open('input.txt', 'r', encoding='utf-8') as f:
    data = [line.rstrip() for line in f]
    data.pop(1)
    f.close()

instructions = data[0]


data = data[1:]
#Make a dict
nodes = {}
for line in data:
    node_id, nexts = line.split(' = ')
    nexts = nexts.replace('(', '').replace(')', '').split(", ")
    nodes[node_id] = {'L': nexts[0], 'R': nexts[1]}

def loopingZ(node):
    steps = 0
    for inst in it.cycle(instructions.strip()):
        steps += 1
        next_node = nodes[node][inst]
        
        node = next_node
        if node.endswith('Z'):
            return steps

currents = [node for node in nodes if node.endswith("A")]
tab = [loopingZ(node) for node in currents]

a = tab[0]
for b in tab[1:]:
    a = (a*b) // gcd(a, b)

print(a)