with open("input.txt", "r") as f:
    file = f.read().strip().splitlines()

num = 0
for i in file:
    card = i.split(": ")[1].split(" | ")
    winning_numbers = set(card[0].strip().replace("  ", " ").split(" "))
    numbers = set(card[1].strip().replace("  ", " ").split(" "))

    intersect = winning_numbers.intersection(numbers)
    if intersect:
        num += 2**(len(intersect) - 1)
    
print(num)
