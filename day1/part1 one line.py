print(sum(int("".join([list(filter(str.isnumeric, i))[j] for j in (0, -1)])) for i in open("input.txt", "r")))
