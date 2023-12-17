import time
def readfile( day):
    file_name = f"input_{day}.txt"
    lines = []
    with open(file_name, mode='r', encoding='utf-8') as f:
        while (line := f.readline()):
            l = [int(n) for n in line.strip()]
            lines.append(l)
    return lines

def take_step(grid, todo, x, y, dx, dy, heatloss, steps, best_visited):
    nx = x + dx
    ny = y + dy
    added = False
    if nx >= 0 and nx < len(grid[0]) and ny >= 0 and ny < len(grid):
        newloss = heatloss + grid[ny][nx]
        if not (nx, ny) in best_visited or best_visited[(nx, ny)] > newloss:
            best_visited[(nx,ny)] = newloss
            if nx != len(grid[0]) - 1 or  ny == len(grid) - 1:
                td = (nx, ny, dx, dy, steps + 1, newloss)
                todo.insert(0, td)
                print(f"    ({x}, {y}, {dx}, {dy}, {steps}, {heatloss} )=>({td}")
                added = True

    if not added:
        if (nx, ny) in best_visited:
            print("Fanns bättre")
        else:
            print("    Går ej")

def traverse(grid):
    todo = [(0,0,1,0,0,0 )]
    best_visited = {}
    best_visited[(0,0)] = 0

    turnl = { (1,0): (0,-1), (-1,0): (0, 1), (0,1): (1,0), (0,-1): (-1,0) }
    turnr = { (1,0): (0,1), (-1, 0): (0,-1), (0, 1): (-1, 0), (0,-1): (1,0)}

    while len(todo) > 0:
        pos = todo.pop(0)
        x,y, dx, dy, steps, heatloss = pos
        print(f"\nWhile {pos}, heatloss {heatloss}")
        # Straight
        print("straight")
        if steps < 3: # straight
            take_step(grid, todo, x, y, dx, dy, heatloss, steps, best_visited)
        else:
            print("    Mer än 3")

        # Right
        print("right")
        ndx, ndy = turnr[(dx, dy)]
        take_step(grid, todo, x, y, ndx, ndy, heatloss, 0, best_visited)

        # Left
        print("Left")
        ndx, ndy = turnl[(dx, dy)]
        take_step(grid, todo, x, y, ndx, ndy, heatloss, 0, best_visited)

    print("17.2 ", best_visited[(len(grid[0])-1, len(grid)-1)] )

def part1():
    lines = readfile(17)
    grid = []

    for line in lines:
            grid.append(list(line))

    for line in grid:
        print(line)

    traverse(grid)

part1()