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

current = 'AAA'
loop = 0
while current != 'ZZZ':
    for inst in instructions:
        current = nodes[current][inst]
        loop += 1

print(loop)
    