from itertools import combinations
with open("input.txt", "r") as f:
    file = f.read().strip().splitlines()

for loop in range(2):
    added = set()
    for y, line in enumerate(file):
        if "#" not in line and y not in added:
            file.insert(y + 1, "."*len(line))
            added.add(y + 1)

    file = ["".join(i) for i in zip(*file[::-1])]

galaxies = []
for y, line in enumerate(file):
    for x, character in enumerate(line):
        if character == "#":
            galaxies.append((x, y))


print(sum(abs(x - ix) + abs(y - iy) for (x, y), (ix, iy) in combinations(galaxies, 2)))
