with open("input.txt", "r") as f:
    file = f.read().strip().splitlines()

values = [0] * len(file)
index = 0
for i in file:
    sequence = [int(i) for i in i.split()]   
    while any(sequence):
        values[index] += sequence[0]
        sequence = [sequence[j] - sequence[j + 1] for j in range(len(sequence) - 1)]
    index += 1   

print(sum(values))
