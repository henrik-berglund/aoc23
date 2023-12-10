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

    new_to_visit = []
    visited_nodes = {}
    visited_nodes[key(x, y)] = 0
    new_to_visit.append((s_x, s_y))

    moves = [
        ((-1,0), ['-', 'L', 'F' ]),
        ((1,0),  ['-', 'J', '7']),
        ((0,-1), ['|', 'F', '7']),
        ((0,1),  ['|', 'L', 'J' ] )]

    dist=-1
    max_dist=0
    while len(new_to_visit) > 0:
        to_visit = new_to_visit
        new_to_visit = []
        dist += 1
        while len(to_visit)> 0:
            node = to_visit.pop(0)
            x, y = node
            visited_nodes[key(x, y)] = dist
            #print(f"dist {dist} checking {x},{y}")
            for m in moves:
                offset, valid_connects = m
                new_x = x + offset[0]
                new_y = y + offset[1]

                #print(f"---about to check {new_x},{new_y}")

                if new_x >= 0 and new_y >= 0 and new_x < len(grid[0]) and new_y < len(grid):
                    c = grid[new_y][new_x]
                    if c in valid_connects:
                        if not key(new_x, new_y) in visited_nodes:
                            new_to_visit.append((new_x,new_y))
                            max_dist = dist + 1

                        #print(f"---added {new_x},{new_y}")

    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if key(x,y) in visited_nodes:
                print(visited_nodes[key(x,y)], " ", end="")
            else:
                print(". ", end="")
        print()

    print("Max dist ", max_dist)
def key(x,y):
    return str(x) + "-" + str(y)

part1()