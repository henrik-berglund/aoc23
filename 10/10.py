def readfile( day):
    file_name = f"input_{day}.txt"
    lines = []
    with open(file_name, mode='r', encoding='utf-8') as f:
        while (line := f.readline()):
            lines.append(line.strip())
    return lines

def part1():
    lines = readfile(10)
    grid = []
    for line in lines:
        grid.append(list(line))
        pass

    for y, line in enumerate(grid):
        print(line)

    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == 'S':
                s_x = x
                s_y = y

    print(key(s_x,s_y))

    to_visit = []
    visited_nodes = {}
    visited_nodes[key(x, y)] = 0

    add_neighbors( grid, to_visit, visited_nodes, s_x, s_y, 0)

#| is a vertical pipe connecting north and south.
#- is a horizontal pipe connecting east and west.
#L is a 90-degree bend connecting north and east.
#J is a 90-degree bend connecting north and west.
#7 is a 90-degree bend connecting south and west.
#F is a 90-degree bend connecting south and east.
#. is ground; there is no pipe in this tile.
def add_neighbors(grid, to_visit, visited_nodes, x, y, dist):

    new_dist = dist+1
    if x > 0:
        new_x = x-1
        new_y = y

        c = grid[new_y][new_y]
        if c in ['-', 'L', 'F' ]:
            if not key(new_x, new_y) in visited_nodes:
                to_visit.append((new_x,new_y, new_dist))

    if x+1 <  len(grid[0]):
        new_x = x+1
        new_y = y

        c = grid[new_y][new_y]
        if c in ['-', 'J', '7' ]:
            if not key(new_x, new_y) in visited_nodes:
                to_visit.append((new_x,new_y, new_dist))

    if y > 0:
        new_x = x
        new_y = y-1

        c = grid[new_y][new_y]
        if c in ['|', 'F', '7' ]:
            if not key(new_x, new_y) in visited_nodes:
                to_visit.append((new_x,new_y, new_dist))

    if y+1 < len(grid):
        new_x = x
        new_y = y+1

        c = grid[new_y][new_y]
        if c in ['|', 'L', 'J' ]:
            if not key(new_x, new_y) in visited_nodes:
                to_visit.append((new_x,new_y, new_dist))

def key(x,y):
    return str(x) + "-" + str(y)

part1()