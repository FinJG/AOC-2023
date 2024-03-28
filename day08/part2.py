from math import lcm

with open("input.txt", "r") as f:
    file = f.read().strip().splitlines()

instructions = [0 if i == "L" else 1 for i in file[0]]

current_nodes = []
network = {}
for line in file[2:]:
    key, nodes = line.split(" = ")
    network[key] = nodes[1:-1].split(", ")

    if key.endswith("A"):
        current_nodes.append(key)

steps = [0] * len(current_nodes)

for i, node in enumerate(current_nodes):
    while not current_nodes[i].endswith("Z"):
        for instruction in instructions:
            if node.endswith("Z"):
                break
            
            current_nodes[i] = network[current_nodes[i]][instruction]
            steps[i] += 1

print(lcm(*steps))
