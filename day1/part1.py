with open("input.txt", "r") as f:
    file = f.read().strip().splitlines()

num = 0
for i in file:
    for j in i:
        if j.isnumeric():
            num += int(j) * 10
            break

    for j in reversed(i):
        if j.isnumeric():
            num += int(j)
            break        
            
print(num)
