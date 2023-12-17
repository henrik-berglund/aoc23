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
    count_energized(0, grid, energized, ray, ray_path)

    print("16.1: ", len(list(energized)))

def part2():
    lines = readfile(16)
    grid = []

    for line in lines:
        if len(line) != 0:
            grid.append(list(line))

    max_count=0
    for y in range(len(grid)):

        ray = (0, y, 1, 0)
        x,y,dx,dy = ray
        energized = set()
        count_energized(0, grid, energized, ray)
        count = len(list(energized))
        print(f"{x},{y} {dx},{dy}: ", count, flush=True)
        if count > max_count:
            max_count = count

        ray = (len(grid[0])-1, y, -1, 0)
        x,y,dx,dy = ray

        energized = set()
        count_energized(0, grid, energized, ray)
        count = len(list(energized))
        print(f"{x},{y} {dx},{dy}: ", count, flush=True)
        if count > max_count:
            max_count = count

    for x in range(len(grid[0])):

        ray = (x, 0, 0, 1)
        x,y,dx,dy = ray
        energized = set()
        count_energized(0, grid, energized, ray)
        count = len(list(energized))
        print(f"{x},{y} {dx},{dy}: ", count, flush=True)
        if count > max_count:
            max_count = count

        ray = (x, len(grid)-1, 0, -1)
        x,y,dx,dy = ray

        energized = set()
        count_energized(0, grid, energized, ray)
        count = len(list(energized))
        print(f"{x},{y} {dx},{dy}: ", count, flush=True)
        if count > max_count:
            max_count = count

    print("16.2: ", max_count)

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


def count_energized(count, grid, ener, ray):
    width = len(grid[0])
    height = len(grid)

    to_process = []
    to_process.append(ray)

    ray_path= []

    dopop = True
    ray1 = None
    ray2 = None
    while len(to_process) > 0  or  ray1:

        if ray1:
            ray = ray1
        else:
            ray =  to_process.pop(0)

        x, y, dx, dy = ray

        ray1 = None
        ray2 = None

        if x == width or y == height or x == -1 or y== -1:
            continue

        if ray in ray_path:
            continue
        else:
            ray_path.append(ray)

        # for prev in previous_paths:
        #     if False: #ray in prev:
        #         index = prev.index(ray)
        #         to_copy = prev[index:]
        #         ray_path.extend(to_copy)
        #
        #         for c in to_copy:
        #             cx, cy, cdx, cdy = c
        #             ener.add((cx, cy))
        #
        #     dopop = len(rays) > 0
        #     continue


        ener.add((x,y))

        c = grid[y][x]
        count += 1

        if c == '.' or (c == '|' and dy != 0 ) or (c == '-' and dx != 0 ):
            x += dx
            y += dy
            ray1 = (x, y, dx, dy)
        elif c == '|':
            ray1 = (x, y-1, 0, -1)
            to_process.append(ray1)

            ray2 = (x, y+1, 0, +1)
            to_process.append(ray2)
        elif c == '-':

            ray1 = (x-1, y, -1, 0)
            to_process.append(ray1)

            ray2 = (x+1, y, 1, 0)
            to_process.append(ray2)

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