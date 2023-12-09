with open("input.txt", "r") as f:
    file = f.read().strip().splitlines()

instructions = [0 if i == "L" else 1 for i in file[0]]
network = {i[0:3]: i[7:-1].split(", ") for i in file[2:]}

steps = 0
current_node = "AAA"
while current_node != "ZZZ":
    for i in instructions:
        current_node = network[current_node][i]
        steps += 1

print(steps)
