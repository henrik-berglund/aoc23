import time
def readfile( day):
    file_name = f"input_{day}.txt"
    lines = []
    with open(file_name, mode='r', encoding='utf-8') as f:
        while (line := f.readline()):
            lines.append(line.strip())
    return lines

def part1():
    lines = readfile(16)
    grid = []

    for line in lines:
        if len(line) != 0:
            grid.append(list(line))

    for line in grid:
        print(line)

    ray = (0,0, 1,0)
    energized = set()

    count_energized(0, grid, energized, ray )

    print("16.1: ", len(list(energized)))

def count_energized(count, grid, ener, ray):
    width = len(grid[0])
    height = len(grid)

    rays = []
    rays.append(ray)

    dopop = True
    ray1 = None
    ray2 = None
    while len(rays) > 0 or dopop == False:
        if dopop:
            ray =  rays.pop(0)
        else:
            ray = ray1

        x, y, dx, dy = ray

        ray1 = None
        ray2 = None

        dopop = False
        if x == width or y == height or x == -1 or y== -1:
            dopop = True
            continue

        c = grid[y][x]
        #print(f"rays {rays} ")
        ltype = '- pop' if dopop else '-'
        print(f"- {ltype} {ray} meets {c}", flush=True, end="")
        count += 1

        if c == '.' or (c == '|' and dy != 0 ) or (c == '-' and dx != 0 ):

            if c != '.':
                ener.add(f"{x}-{y}")

            x += dx
            y += dy
            #count_energized(count, grid,ener,   )
            ray1 = (x, y, dx, dy)

            print("=> ray ", ray1)

        elif c == '|':
            ener.add(f"{x}-{y}")

            ray1 = (x, y-1, 0, -1)
            #print(f"{count} r1=> {ray}", flush=True)
            rays.append(ray1)
            #count_energized(count, grid, ener, ray)

            ray2 = (x, y+1, 0, +1)
            #print(f"{count} r2=> {ray}", flush=True)
            #count_energized(count, grid, ener, ray)
            rays.append(ray2)

            print("=> ray1 ", ray1, " ray2 ", ray2)

        elif c == '-':
            ener.add(f"{x}-{y}")

            ray1 = (x-1, y, -1, 0)
            #print(f"{count} r1=> {ray}")
            #count_energized(count,grid, ener, ray)
            rays.append(ray1)

            ray2 = (x+1, y, 1, 0)
            #print(f"{count} r2=> {ray}")
            #count_energized(count, grid, ener, ray)
            rays.append(ray2)
            print("=> ray1 ", ray1, " ray2 ", ray2)

        elif c == '/':
            new_dir = {'1,0': (0,-1), '-1,0': (0,1), '0,1': (-1,0),  '0,-1': (1,0)}
            ener.add(f"{x}-{y}")

            key = f"{dx},{dy}"
            dx, dy = new_dir[key]

            ray1 = (x+dx, y+dy, dx, dy)
            #print(f"{count} r=> {ray}")

            #count_energized(count, grid, ener, ray)
            #rays.append(ray)
            print("=> ray1 ", ray1)

        elif c == '\\':
            new_dir = {'1,0': (0,1), '-1,0': (0,-1), '0,1': (1,0),  '0,-1': (-1,0)}
            ener.add(f"{x}-{y}")

            key = f"{dx},{dy}"
            dx, dy = new_dir[key]

            ray1 = (x+dx, y+dy, dx, dy)
            #print(f"{count} r=> {ray}")

            #count_energized(count, grid, ener,ray)
            #rays.append(ray)
            print("=> ray1 ", ray1)

        print(f"{count}------------------------")
        for iy, l in enumerate(grid):
            for ix, c in enumerate(l):
                printed = False
                r = ray
                if r:
                    rx, ry, drx, dry = r
                    if rx == ix and ry == iy:
                        print(' X ', end='')
                        printed = True
                if not printed:
                    print(f" {c} ", end='')
            print()


part1()
