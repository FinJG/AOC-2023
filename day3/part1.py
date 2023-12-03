import math

with open("input.txt", "r") as f:
    file = f.read().strip().splitlines()

num = ""
coords = []

digits = []
symbols = []

for y, line in enumerate(file):
    for x, each in enumerate(line):
        if each.isnumeric():
            num += each
            coords.append((x, y))


        elif num:
            digits.append((int(num), coords))
            coords = []
            num = ""

        if each.isnumeric() is False and each != ".":
            symbols.append((x, y))

sums = 0
for digit in digits:
    for coord in symbols:
        for j in digit[1]:
            if math.dist(j, coord) < 2:
                sums += digit[0]
                break   

print(sums)
