import time
def readfile( day):
    file_name = f"input_{day}.txt"
    lines = []
    with open(file_name, mode='r', encoding='utf-8') as f:
        while (line := f.readline()):
            l = [int(n) for n in line.strip()]
            lines.append(l)
    return lines

def max_best(grid):
    w=0
    y = 0
    for x in range(1, len(grid[0])):
        w += grid[y][x]
        print(f"{x},{y}: {w}")

        y+= 1
        w += grid[y][x]
        print(f"{x},{y}: {w}")
    return w

def take_step(grid, todo, x, y, dx, dy, heatloss, steps, best_visited, best_found, log):
    nx = x + dx
    ny = y + dy
    add = False
    if nx >= 0 and nx < len(grid[0]) and ny >= 0 and ny < len(grid):
        new_loss = heatloss + grid[ny][nx]

        if new_loss >= best_found:
            return best_found

        new_steps = steps+1
        if not (nx, ny, dx, dy ) in best_visited:
            add = True
            best_visited[(nx, ny, dx, dy )] = []
        else:
            visited = best_visited[(nx, ny, dx, dy )]
            add = True
            for v in visited:
                best_loss, best_steps= v
                #if log:
                #    print("Checking prev")

                if best_loss <= new_loss and best_steps <= new_steps:
                    add = False
                    if log:
                        print("Pruning at ", (nx, ny, dx, dy ))
                #if log and add:
                #    print("Not found")


        if add:
            td = (nx, ny, dx, dy, new_steps, new_loss)
            todo.insert(0, td)
            best_visited[(nx, ny, dx, dy)].append((new_loss, new_steps))

            if nx == len(grid[0])-1 and ny == len(grid)-1:
                if new_loss < best_found:
                    print("*** new best ", new_loss, flush=True)
                    best_found = new_loss

            if log:
                print(f"    ({x}, {y}, {dx}, {dy}, {steps}, {heatloss} )=>({td}")

    return best_found

def traverse(grid):
    todo = [(0,0,1,0,0,0 )]
    best_visited = {}

    turnl = { (1,0): (0,-1), (-1,0): (0, 1), (0,1): (1,0), (0,-1): (-1,0) }
    turnr = { (1,0): (0,1), (-1, 0): (0,-1), (0, 1): (-1, 0), (0,-1): (1,0)}
    best_found = max_best(grid)

    while len(todo) > 0:
        pos = todo.pop(0)
        x,y, dx, dy, steps, heatloss = pos
        # Straight

        log = False
        #if (x,y) ==(4,1):
        #log = True

        if log:
            print(f"\nPopped {pos}, heatloss {heatloss}")

        if log:
            print("continue straight")

        if steps < 10: # straight
            best_found = take_step(grid, todo, x, y, dx, dy, heatloss,
                                   steps, best_visited, best_found, log)
        elif log:
            print(f"    Mer än 3: {steps}")
            pass

        # Right
        if steps >= 4:
            if log:
                print("right")

            ndx, ndy = turnr[(dx, dy)]
            best_found = take_step(grid, todo, x, y, ndx, ndy, heatloss,
                           0, best_visited, best_found, log)

        # Left

        if steps >= 4:
            ndx, ndy = turnl[(dx, dy)]
            if log:
                print("Left")

            best_found = take_step(grid, todo, x, y, ndx, ndy, heatloss,
                               0, best_visited, best_found, log)

    print("17.1 ", best_found)

#    for pos in [(1,0), (2,0), (2,1), (3,1), (4,1), (5,1), (5,0), (6,0), (7,0), (8,0), (8,1), (8,2)]:
#        for v in best_visited[pos]:
#            print(f"{pos}: {best_visited[pos]}")

def part1():
    lines = readfile(17)
    grid = []

    for line in lines:
            grid.append(list(line))

    #for line in grid:
    #    print(line)
    start = time.time()
    traverse(grid)
    print("Time: ", time.time()-start)

part1()

