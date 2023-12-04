with open("input.txt", "r") as f:
    file = f.read().strip().splitlines()

lis = [1] * len(file)

for i, v in enumerate(file):
    card = v.split(": ")[1].split(" | ")

    winning_numbers = set(card[0].strip().replace("  ", " ").split(" "))
    numbers = set(card[1].strip().replace("  ", " ").split(" "))

    intersect = winning_numbers.intersection(numbers)

    if intersect:
        for j in range(1, len(intersect) + 1):
                lis[j + i] += lis[i]

print(sum(lis))
