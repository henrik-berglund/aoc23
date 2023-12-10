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
                break

    print(key(x,y))

    to_visit = []
    visited_nodes = []
    dist = {}
    visited_nodes[key(x, y)] = 0

    add_neighbors( to_visit,  visited_nodes, x, y, 0)

def add_neighbors(to_visit, visited_nodes, x, y, 0):
    pass


def key(x,y):
    return str(x) + "-" + str(y)

part1()