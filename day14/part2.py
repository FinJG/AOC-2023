with open("input.txt", "r") as f:
    file = f.read().strip().splitlines()

def move(axis, direction, board):
    board = [list(i) for i in board]

    if direction and not axis:
        board = [i[::-1] for i in board]

    elif direction:
        board = board[::-1]

    for iy, y in enumerate(board):
        for ix, x in enumerate(y):
            index = 0
            if x == "O":
                if axis:
                    for i in range(iy + 1):     
                        if board[iy - i][ix] == ".":
                            index = i 
                        if board[iy - i][ix] == "#":
                            break
                    board[iy][ix], board[iy - index][ix] = board[iy - index][ix], board[iy][ix]
                        
                else:
                    for i in range(ix + 1):
                        if board[iy][ix - i] == ".":
                            index = i
                        if board[iy][ix - i] == "#":
                            break

                    board[iy][ix], board[iy][ix - index] = board[iy][ix - index], board[iy][ix]

    if direction and not axis:
        board = [i[::-1] for i in board]

    elif direction:
        board = board[::-1]

    return board


cycle = ((True, False), (False, False), (True, True), (False, True))

states = []
first = False

while True:
    for j in cycle:
        file = move(j[0], j[1], file)

    if file not in states:
        states.append(file)

    else:
        if first:
            break
        start = len(states)
        states = []
        first = True

def get_sum(state):
    total = 0
    for i, line in enumerate(state):
        total += (len(state) - i) * line.count("O")
    return total

cycle_num = 1000000000
ans_index = (cycle_num) % len(states) + (len(states) * ((start + 1) // len(states)))
print([get_sum(state) for state in states][(ans_index - 1) - (start + 1)])

