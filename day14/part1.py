with open("input.txt", "r") as f:
    file = f.read().strip().splitlines()

def move(board):
    for iy, y in enumerate(board):
        for ix, x in enumerate(y):
            index = 0
            if x == "O":
                for i in range(iy + 1):
                    if board[iy - i][ix] == ".":
                        index = i 
                    if board[iy - i][ix] == "#":
                        break
                board[iy][ix], board[iy - index][ix] = board[iy - index][ix], board[iy][ix]
    return board

total = 0
file = [[i for i in j] for j in file]
for i, line in enumerate(move(file)):
    total += (len(file) - i) * line.count("O")

print(total)