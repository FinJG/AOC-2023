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

        if each == "*":
            symbols.append((x, y))

sums = 0
for coord in symbols:
    gear = []
    for digit in digits:
        for j in digit[1]:
            if math.dist(j, coord) < 2:
                gear.append(digit[0])
                break

    gear_ratio = 1
    if len(gear) > 1:
        for i in gear:
            gear_ratio *= i
        sums += gear_ratio

        
print(sums)
