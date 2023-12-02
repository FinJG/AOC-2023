with open("input.txt", "r") as f:
    file = f.read().strip().splitlines()

num = 0
for i in file:
    compare = {
        "red":0,
        "green":0,
        "blue":0
        }

    for group in i.split(": ")[1].split("; "):
        for colour in group.split(", "):
            value = colour.split(" ")
            compare[value[1]] = max(int(value[0]), compare[value[1]])

    power = 1
    for i in compare.values():
        power *= i

    num += power

print(num)
