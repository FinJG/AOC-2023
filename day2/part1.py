with open("input.txt", "r") as f:
    file = f.read().strip().splitlines()

compare = {
    "red":12,
    "green":13,
    "blue":14
}

num = 0
for i, v in enumerate(file):
    game = v.split(": ")[1]
    valid_game = True

    for group in game.split("; "):
        for colour in group.split(", "):
            value = colour.split(" ")

            if int(value[0]) > compare[value[1]]:
                valid_game = False
                break

    if valid_game:
        num += i + 1

print(num)
