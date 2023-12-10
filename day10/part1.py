with open("input.txt", "r") as f:
    file = f.read().strip().splitlines()

pipes = {
    "|":((0, -1), (0, 1)),
    "-":((-1, 0), (1, 0)),
    "L":((0, -1), (1, 0)),
    "J":((0, -1), (-1, 0)),
    "7":((-1, 0), (0, 1)),
    "F":((1, 0), (0, 1)),
    ".":((0, 0), (0, 0)),
    "S":((0, 0), (0, 0))
}

path = []
for y, line in enumerate(file):
    if "S" in line:
        path.append((y, line.index("S")))

def get_next_pipe():
    if file[path[-1][0]][path[-1][1]] == "S":
        for x, y in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            if (path[-1][1] - (path[-1][1] + x), path[-1][0] - (path[-1][0] + y)) in pipes[file[path[-1][0] + y][path[-1][1] + x]]:
                path.append((path[-1][0] + y, path[-1][1] + x))
                return None

    for x, y in pipes[file[path[-1][0]][path[-1][1]]]:
        if (-x, -y) in pipes[file[path[-1][0] + y][path[-1][1] + x]] and (path[-1][0] + y, path[-1][1] + x) not in path:
            path.append((path[-1][0] + y, path[-1][1] + x))
            return None
        
        if file[path[-1][0] + y][path[-1][1] + x] == "S" and len(path) > 2:
            return "loop found"


while get_next_pipe() != "loop found":
    pass

print(len(path) / 2)
