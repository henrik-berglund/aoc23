import matplotlib.pyplot as plt

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
    visited_nodes[key(s_x, s_y)] = 0
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
            print("top loop: ", "10-8" in visited_nodes)

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
                            print(f"***added {new_x}-{new_y} from {x},{y}")
                            max_dist = dist + 1

                        #print(f"---added {new_x},{new_y}")
    print("what3: ", "10-8" in visited_nodes)
    print(visited_nodes.keys())

    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if key(x,y) in visited_nodes:
                print(visited_nodes[key(x,y)], " ", end="")
            else:
                print(". ", end="")
        print()

    print("Max dist ", max_dist)

    print("what2: ", "10-8" in visited_nodes)

    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if key(x,y) in visited_nodes:
                print(" X ", end="")
            else:
                c = count(x, y, visited_nodes, grid)
                print(f"{c:3}", end="")
        print()

    print("what1: ", "10-8" in visited_nodes)
    plot(grid, visited_nodes)

def count(x, y, visited, grid):

    count =0
    for mx in range(x+1, len(grid[0])):
        if key(mx, y) in visited:
            count += 1

    for mx in range(0, x-1):
        if key(mx, y) in visited:
            count += 1

    for my in range(y+1, len(grid)):
        if key(x, my) in visited:
            count += 1

    for my in range(0, y-1):
        if key(x, my) in visited:
            count += 1

    return count

def key(x,y):
    return str(x) + "-" + str(y)



def plot(grid, visited):
    # Define the range of x and y values to check
    x_range = range(0, len(grid[0]))
    y_range = range(0, len(grid))

    # Prepare lists to store loop points and non-loop points
    loop_points_x = []
    loop_points_y = []
    non_loop_points_x = []
    non_loop_points_y = []

    # Check each point in the grid
    for x in x_range:
        for y in y_range:
            print(f"{key(x,y)} {key(x,y) in visited}")
            if key(x,y) in visited:
                loop_points_x.append(x)
                loop_points_y.append(y)
            else:
                non_loop_points_x.append(x)
                non_loop_points_y.append(y)

    # Plotting
    plt.scatter(loop_points_x, loop_points_y, color='blue', label='Loop Points')  # Loop points in blue
    plt.scatter(non_loop_points_x, non_loop_points_y, color='red', label='Non-loop Points')  # Non-loop points in red
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Visualization of the Loop Structure')
    plt.legend()
    plt.grid(False)
    plt.show()






part1()