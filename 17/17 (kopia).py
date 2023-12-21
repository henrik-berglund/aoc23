import time
def readfile( day):
    file_name = f"input_{day}.txt"
    lines = []
    with open(file_name, mode='r', encoding='utf-8') as f:
        while (line := f.readline()):
            l = [int(n) for n in line.strip()]
            lines.append(l)
    return lines

def take_step(grid, todo, x, y, dx, dy, heatloss, steps, best_visited, best_found, path, log):
    nx = x + dx
    ny = y + dy
    added = False
    if nx >= 0 and nx < len(grid[0]) and ny >= 0 and ny < len(grid):
        newloss = heatloss + grid[ny][nx]

        if (nx, ny) in best_visited:
            best_loss, best_steps, best_path = best_visited[(nx, ny)]
        else:
            best_loss, best_steps, best_path = (None, None, None)

        if best_loss and best_loss < newloss:
            if log:
                print("Pruning at ", best_found)
            pass
        elif not best_loss or best_loss > newloss or (best_loss == newloss and best_steps > (steps+1)):
            best_visited[(nx,ny)] = (newloss, steps+1, path)

            if (nx == len(grid[0]) - 1) and  (ny == len(grid) - 1):
                best_found = newloss
                #print(f"Best path to {nx} {ny}: ", path + [(nx,ny)])
            else:
                td = (nx, ny, dx, dy, steps + 1, newloss, path + [(nx,ny)])
                todo.insert(0, td)
                if log:
                    print(f"    ({x}, {y}, {dx}, {dy}, {steps}, {heatloss} )=>({td}")
                added = True

    if not added:
        if (nx, ny) in best_visited:
            if log:
                print("    Fanns bättre")
            pass
        else:
            if log:
                print("    Går ej")
            pass
    return best_found

def traverse(grid):
    todo = [(0,0,1,0,0,0,[] )]
    best_visited = {}
    best_visited[(0,0)] = (0, [])

    turnl = { (1,0): (0,-1), (-1,0): (0, 1), (0,1): (1,0), (0,-1): (-1,0) }
    turnr = { (1,0): (0,1), (-1, 0): (0,-1), (0, 1): (-1, 0), (0,-1): (1,0)}
    best_found = 9999999999999

    while len(todo) > 0:
        pos = todo.pop(0)
        x,y, dx, dy, steps, heatloss, path = pos
        # Straight

        log = False
        if (x,y) ==(4,1):
            log = True

        if log:
            print(f"\nWhile {pos}, heatloss {heatloss}")

        if log:
            print("straight")

        if steps < 3: # straight
            best_found = take_step(grid, todo, x, y, dx, dy, heatloss,
                                   steps, best_visited, best_found, path, log)
        elif log:
            print(f"    Mer än 3: {steps}")
            pass

        # Right
        if log:
            print("right")
        ndx, ndy = turnr[(dx, dy)]
        best_found = take_step(grid, todo, x, y, ndx, ndy, heatloss,
                               -1, best_visited, best_found, path, log)

        # Left
        if log:
            print("Left")
        ndx, ndy = turnl[(dx, dy)]
        best_found = take_step(grid, todo, x, y, ndx, ndy, heatloss,
                               -1, best_visited, best_found, path, log)

    print("17.2 ", best_visited[(len(grid[0])-1, len(grid)-1)]  )

    for pos in [(1,0), (2,0), (2,1), (3,1), (4,1), (5,1), (5,0), (6,0), (7,0), (8,0), (8,1), (8,2)]:
        print(f"{pos}: {best_visited[pos]}")

def part1():
    lines = readfile(17)
    grid = []

    for line in lines:
            grid.append(list(line))

    for line in grid:
        print(line)

    traverse(grid)

part1()