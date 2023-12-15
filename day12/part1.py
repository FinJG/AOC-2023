with open("input.txt", "r") as f:
    file = f.read().strip().splitlines()


def place(springs, total):
    start = total - springs[0]

    if len(springs) == 1:
        return [("." * i + "#" * springs[0] + "." * (start - i)) for i in range(start + 1)]

    ans = []
    
    for i in range(total - springs[0]):
        for sol in place(springs[1:], start - i - 1):
            thing = "." * i + "#" * springs[0] + "." + sol

            ans.append(thing)
    
    return ans

num = 0
for line in file:
    spring, data = line.split()
    data = data.split(",")
    
    known_spots = [i for i, v in enumerate(spring) if v == "#"]
    empty_spots = [i for i, v in enumerate(spring) if v == "."]


    for i in place([int(i) for i in data], len(spring)):
        if all([True if i[j] == "#" else False for j in known_spots]):
            if all([True if i[j] != "#" else False for j in empty_spots]):
                num += 1
        # print(len(i))
print(num)
