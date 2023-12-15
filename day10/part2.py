with open("input.txt", "r") as f:
    file = f.read().strip().splitlines()

pipes = {
    "|":((0, -1), (0, 1)),
    "-":((-1, 0), (1, 0)),
    "L":((0, -1), (1, 0)),
    "J":((0, -1), (-1, 0)),
    "7":((-1, 0), (0, 1)),
    "F":((1, 0), (0, 1)),
    ".":None,
    "S":((0, -1), (0, 1), (-1, 0), (1, 0))
}

path = []
for y, line in enumerate(file):
    if "S" in line:
        path.append((y, line.index("S")))
        break

    
def get_next_pipe(pipe):
    for x, y in pipes[file[pipe[0]][pipe[1]]]:
        if (-x, -y) in pipes[file[pipe[0] + y][pipe[1] + x]] and (pipe[0] + y, pipe[1] + x) not in path:
            path.append((pipe[0] + y, pipe[1] + x))
            return True
    return False

while get_next_pipe(path[-1]):pass

n = len(path)
area = 0
j = n - 1
for i in range(n):
    area += (path[j][0] + path[i][0]) * (path[j][1] - path[i][1])
    j = i

print(abs(area // 2) - (len(path) // 2) + 1)
