with open("input.txt", "r") as f:
    file = f.read().split(",")

total = 0
for line in file:
    current_value = 0
    for character in line:
        current_value = ((current_value + ord(character)) * 17) % 256
    total += current_value

print(total)
