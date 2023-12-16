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

    count_energized(0, grid,energized, ray )

    print("16.1: ", len(list(set)))

def count_energized(count, grid, ener, ray):
    x, y, dx, dy = ray
    width = len(grid[0])
    height = len(grid)

    rays = []
    rays.add(ray)
    
    if x == width or y == height or x == -1 or y== -1:
        return

    c = grid[y][x]
    print(f"dir {ray} meets {c}", flush=True)
    count += 1

    if c == '.' or (c == '|' and dy != 0 ) or (c == '-' and dx != 0 ):

        if c != '.':
            ener.add(f"{x}-{y}")

        x += dx
        y += dy
        count_energized(count, grid,ener,  (x, y, dx, dy) )
    elif c == '|':
        ener.add(f"{x}-{y}")

        ray = (x, y-1, 0, -1)
        print(f"{count} r1=> {ray}", flush=True)
        count_energized(count, grid, ener, ray)

        ray = (x, y+1, 0, +1)
        print(f"{count} r2=> {ray}", flush=True)
        count_energized(count, grid, ener, ray)

    elif c == '-':
        ener.add(f"{x}-{y}")

        ray = (x-1, y, -1, 0)
        print(f"{count} r1=> {ray}")
        count_energized(count,grid, ener, ray)

        ray = (x+1, y, 1, 0)
        print(f"{count} r2=> {ray}")
        count_energized(count, grid, ener, ray)

    elif c == '/':
        new_dir = {'1,0': (0,-1), '-1,0': (0,1), '0,1': (-1,0),  '0,-1': (1,0)}
        ener.add(f"{x}-{y}")

        key = f"{dx},{dy}"
        dx, dy = new_dir[key]

        ray = (x+dx, y+dy, dx, dy)
        print(f"{count} r=> {ray}")

        count_energized(count, grid, ener, ray)

    elif c == '\\':
        new_dir = {'1,0': (0,1), '-1,0': (0,-1), '0,1': (1,0),  '0,-1': (-1,0)}
        ener.add(f"{x}-{y}")

        key = f"{dx},{dy}"
        dx, dy = new_dir[key]

        ray = (x+dx, y+dy, dx, dy)
        print(f"{count} r=> {ray}")

        count_energized(count, grid, ener,ray)


part1()
