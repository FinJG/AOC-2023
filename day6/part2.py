with open("input.txt", "r") as f:
    file = f.read().strip().splitlines()

time = int(file[0][5:].replace(" ", ""))
distance = int(file[1][9:].replace(" ", ""))

shortest = 0
while True:
    if (time - shortest) * shortest > distance:
        break
    shortest += 1

print((time - shortest) - shortest + 1)
