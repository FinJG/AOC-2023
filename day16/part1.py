with open("input.txt", "r") as f:
    file = f.read().strip().splitlines()

beam_pos = (0, 0)
beam_direction = (1, 0)
energized_tiles = set()

def move(beam_direction, beam_pos):
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
            move((-1, 0), beam_pos)
            move((1, 0), beam_pos)

        if file[beam_pos[1]][beam_pos[0]] == "|":
            beam_direction = (0, 1)
            move((0, -1), beam_pos)
            move((0, 1), beam_pos)
            


move(beam_direction, beam_pos)


print(len(energized_tiles))

