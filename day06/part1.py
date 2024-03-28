with open("input.txt", "r") as f:
    file = f.read().strip().splitlines()

times = [int(i) for i in file[0][5:].strip().split()]
distances = [int(i) for i in file[1][9:].strip().split()]

total = 1
for i, time in enumerate(times):
    shortest = 0
    while True:
        if (time - shortest) * shortest > distances[i]:
            break
        shortest += 1

    total *= (time - shortest) - shortest + 1

print(total)
