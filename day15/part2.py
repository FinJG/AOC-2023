with open("input.txt", "r") as f:
    file = f.read().split(",")

boxes = [{} for _ in range(256)]
for line in file:
    line = line.replace("-", "").split("=")
    
    box = 0
    for character in line[0]:
        box = ((box + ord(character)) * 17) % 256

    if len(line) == 2:
        boxes[box][line[0]] = int(line[1])
    else:
        boxes[box].pop(line[0], None)

total = 0
for i, v in enumerate(boxes, 1):
    for ij, j in enumerate(v.values(), 1):
        total += i * ij * j

print(total)
