with open("input.txt", "r") as f:
    file = f.read().strip().splitlines()

num = 0
for i in file:
    for lis, multiple in ((i, 10), (reversed(i), 1)):
        for j in lis:
            if j.isnumeric():
                num += int(j) * multiple
                break
            
print(num)
