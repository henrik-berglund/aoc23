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

    add_neighbors( to_visit, visited_nodes, s_x, s_y, 0)

def add_neighbors(to_visit, visited_nodes, x, y, dist):
    pass


def key(x,y):
    return str(x) + "-" + str(y)

part1()