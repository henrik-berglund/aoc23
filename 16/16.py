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

    ray_path = []
    previous_paths = []
    count_energized(0, grid, energized, ray, ray_path, previous_paths )

    print("16.1: ", len(list(energized)))

def part2():
    lines = readfile(16)
    grid = []

    for line in lines:
        if len(line) != 0:
            grid.append(list(line))

    x=0
    max_count=0
    dx = 1
    dy = 0
    previous_paths = []
    for y in range(10):
        ray = (x, y, dx, dy)
        path = []
        energized = set()
        count_energized(0, grid, energized, ray, path, previous_paths)
        previous_paths.append(path)
        count = len(list(energized))
        print(f"{x},{y} {dx},{dy}: ", count, flush=True)
        if count > max_count:
            max_count = count
    return


    max_count = 0
    for y in [0, len(grid)-1]:
        for x in range(len(grid[0])):
            for d in [(0, 1), (0,-1)]:
                dx, dy = d
                ray = (x,y,dx,dy)
                energized = set()
                count_energized(0, grid, energized, ray)

                count = len(list(energized))
                print("new ", count, flush=True)
                if count > max_count:
                    max_count = count

    for x in [0, len(grid[0])-1]:
        for y in range(len(grid)):
            for d in [(1, 0), (-1,0)]:
                dx, dy = d
                ray = (x,y,dx,dy)
                energized = set()
                count_energized(0, grid, energized, ray)

                count = len(list(energized))
                print("new ", count, flush=True)
                if count > max_count:
                    max_count = count


    print(max_count)


    print("16.2: ", max_count)


def count_energized(count, grid, ener, ray, ray_path, previous_paths):
    width = len(grid[0])
    height = len(grid)

    rays = []
    rays.append(ray)

    dopop = True
    ray1 = None
    ray2 = None
    while len(rays) > 0 or not dopop:

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


        if ray in ray_path:
            dopop = True
            continue
        ray_path.append(ray)

        ener.add((x,y))

        c = grid[y][x]
        count += 1

        if c == '.' or (c == '|' and dy != 0 ) or (c == '-' and dx != 0 ):
            x += dx
            y += dy
            ray1 = (x, y, dx, dy)
        elif c == '|':
            ray1 = (x, y-1, 0, -1)
            rays.append(ray1)

            ray2 = (x, y+1, 0, +1)
            rays.append(ray2)
        elif c == '-':

            ray1 = (x-1, y, -1, 0)
            rays.append(ray1)

            ray2 = (x+1, y, 1, 0)
            rays.append(ray2)

        elif c == '/':
            new_dir = {(1,0): (0,-1), (-1,0): (0,1), (0,1): (-1,0),  (0,-1): (1,0)}

            key = (dx, dy)
            dx, dy = new_dir[key]

            ray1 = (x+dx, y+dy, dx, dy)

        elif c == '\\':
            new_dir = {(1,0): (0,1), (-1,0): (0,-1), (0,1): (1,0),  (0,-1): (-1,0)}

            key = (dx,dy)
            dx, dy = new_dir[key]

            ray1 = (x+dx, y+dy, dx, dy)


start = time.time()
part2()
print("Time: ", time.time()-start)