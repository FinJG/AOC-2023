from itertools import combinations
with open("input.txt", "r") as f:
    file = f.read().strip().splitlines()

galaxies = set()
for y, line in enumerate(file):
    for x, character in enumerate(line):
        if character == "#":
            galaxies.add((x, y))
            
expansion = []
for loop in range(2):
    added = set()
    for y, line in enumerate(file):
        if "#" not in line:
            added.add(y)

    file = ["".join(i) for i in zip(*file[::-1])]
    expansion.insert(0, added)



num = 0
for (x, y), (ix, iy) in combinations(galaxies, 2):
    num_of_expantions = 0
    for i, loop in enumerate(expansion):
        galax = ((x, y)[i], (ix, iy)[i])
        big = max(*galax)
        small = min(*galax)
        rang = range(small, big)
        for gap in loop:
            if gap in rang:
                num_of_expantions += 1
   
    num += abs(x - ix) + abs(y - iy) + (num_of_expantions * 999999)

print(num)
