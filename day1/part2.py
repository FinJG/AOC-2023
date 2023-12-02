with open("input.txt", "r") as f:
    file = f.read().strip().splitlines()

dic = {"one":"o1e",
       "two":"t2o",
       "three":"t3e",
       "four":"f4r",
       "five":"f5e",
       "six":"s6x",
       "seven":"s7n",
       "eight":"e8t",
       "nine":"n9e"
       }

num = 0
for i in file:
    for key in dic:
        if key in i:
            i = i.replace(key, dic[key])

    for j in i:
        if j.isnumeric():
            num += int(j) * 10
            break

    for j in reversed(i):
        if j.isnumeric():
            num += int(j)
            break       

print(num)
