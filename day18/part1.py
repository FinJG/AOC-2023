with open("input.txt", "r") as f:
    file = f.read().strip().splitlines()

directions = {
    "R":(1, 0),
    "L":(-1, 0),
    "U":(0, -1),
    "D":(0, 1)
}

pos = [0, 0]
coords = []
perimeter = 0
for line in file:
    direction, steps = line.split()[:2]

    facing = directions[direction]
    pos[0] += facing[0] * int(steps)
    pos[1] += facing[1] * int(steps)
    perimeter += int(steps)
    coords.append(pos.copy())

n = len(coords)
area = 0
j = n - 1
for i in range(n):
    area += (coords[j][0] + coords[i][0]) * (coords[j][1] - coords[i][1])
    j = i

print(int(abs(area // 2) + (perimeter / 2) + 1))
