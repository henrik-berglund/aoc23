import time
def readfile( day):
    file_name = f"input_{day}.txt"
    lines = []
    with open(file_name, mode='r', encoding='utf-8') as f:
        while (line := f.readline()):
            lines.append(line.strip())
    return lines


def part1():
    lines = readfile(18)
    instr = []
    for line in lines:
        s1 = line.split(" ")
        instr.append((s1[0], int(s1[1]), s1[2][1:-1]))

    coords = [(0,0)]
    x = 0
    y = 0
    dir = {'R': (1,0), 'U' : (0,-1), 'D': (0,1), 'L': (-1,0)}
    for i in instr:
        d, l, col = i
        dx, dy = dir[d]
        for j in range(l):
            x += dx
            y += dy
            coords.append((x,y))

    max_x =0
    max_y = 0
    for c in coords:
        x,y = c
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    print(max_x, max_y)

    grid = []
    for y in range(max_y+1):
        grid.append(list('.'*(max_x+1)))

    for c in coords:
        x, y = c
        grid[y][x] = '#'

    for y in range(max_y+1):
        print(grid[y])

    #for line in grid:
    #    print(line)

part1()

