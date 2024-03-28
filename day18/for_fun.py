pos = (0, 0)
perimeter = 0
coords = [pos := tuple(map(sum, zip((pos), (i * int(line.split()[:2][1]) for i in {"R":(1, 0),"L":(-1, 0),"U":(0, -1),"D":(0, 1)}[line.split()[:2][0]])))) for line in open("input.txt", "r") if (perimeter := perimeter + int(line.split()[:2][1]))]
print(int((sum((area := (x * coords[(i + 1) % len(coords)][1]) - (coords[(i + 1) % len(coords)][0] * y) for i, (x, y) in enumerate(coords))) / 2) + perimeter / 2 + 1))