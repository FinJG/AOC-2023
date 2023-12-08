with open("input.txt", "r") as f:
    file = f.read().strip().splitlines()

time = int(file[0][5:].replace(" ", ""))
distance = int(file[1][9:].replace(" ", ""))

print(int((-time - (((time * time) - (4 * distance))**0.5)) / -2)
                - -(-(-time + (((time * time) - (4 * distance))**0.5)) // -2) + 1)