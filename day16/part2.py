with open("input.txt", "r") as f:
    file = f.read().strip().splitlines()

def move(beam_direction, beam_pos, energized_tiles):
    while True:
        energized_tiles.add(beam_pos)
        if file[beam_pos[1]][beam_pos[0]] == "\\":
            beam_direction = (beam_direction[1], beam_direction[0])

        elif file[beam_pos[1]][beam_pos[0]] == "/":          
            beam_direction = (-beam_direction[1], -beam_direction[0])

        beam_pos = (beam_pos[0] + beam_direction[0], beam_pos[1] + beam_direction[1])

        if beam_pos[0] > len(file[0]) - 1 or beam_pos[0] < 0:
            return
        if beam_pos[1] > len(file) - 1 or beam_pos[1] < 0:
            return        
        if beam_pos in energized_tiles and file[beam_pos[1]][beam_pos[0]] in "-|":
            break 

        if file[beam_pos[1]][beam_pos[0]] == "-":
            beam_direction = (1, 0)
            move((-1, 0), beam_pos, energized_tiles)
            move((1, 0), beam_pos, energized_tiles)

        if file[beam_pos[1]][beam_pos[0]] == "|":
            beam_direction = (0, 1)
            move((0, -1), beam_pos, energized_tiles)
            move((0, 1), beam_pos, energized_tiles)


def get_energized(beam_direction, beam_pos):
    energized_tiles = set()
    move(beam_direction, beam_pos, energized_tiles)
    return len(energized_tiles)


configurations = set()
for y in range(len(file)):
    for x in range(len(file[0])):
        if y == 0:
            configurations.add(get_energized((0, 1), (x, y)))
        if y == len(file) - 1:
            configurations.add(get_energized((0, -1), (x, y)))
        if x == 0:
            configurations.add(get_energized((1, 0), (x, y)))
        if x == len(file[0]) - 1:
            configurations.add(get_energized((-1, 0), (x, y)))

print(max(configurations))
