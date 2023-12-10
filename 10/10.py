import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon
from matplotlib.path import Path

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

    connects_to_left = ['-', 'J', '7', 'S']
    connects_to_right = ['-', 'L', 'F', 'S' ]
    connects_up = ['|', 'L', 'J', 'S' ]
    connects_down = ['|', 'F', '7', 'S']

    moves = [
        ((-1,0), connects_to_right, connects_to_left),
        ((1,0),  connects_to_left, connects_to_right),
        ((0,-1), connects_down, connects_up),
        ((0,1),   connects_up, connects_down)]

    dist=-1
    max_dist=0
    while len(new_to_visit) > 0:
        to_visit = new_to_visit
        new_to_visit = []
        dist += 1
        while len(to_visit)> 0:
            node = to_visit.pop(0)
            x, y = node
            c_this_node = grid[y][x]
            visited_nodes[key(x, y)] = dist

            for m in moves:
                offset, valid_connects, outgoing_valid_connects = m
                new_x = x + offset[0]
                new_y = y + offset[1]

                if new_x >= 0 and new_y >= 0 and new_x < len(grid[0]) and new_y < len(grid):
                    c = grid[new_y][new_x]
                    if c in valid_connects and c_this_node in outgoing_valid_connects:
                        if not key(new_x, new_y) in visited_nodes:
                            new_to_visit.append((new_x,new_y))
                            max_dist = dist + 1

    print("Max dist ", max_dist)
    #count_inside(grid, visited_nodes)

    plot(grid, visited_nodes)

def part2():
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

    connects_to_left = ['-', 'J', '7', 'S']
    connects_to_right = ['-', 'L', 'F', 'S' ]
    connects_up = ['|', 'L', 'J', 'S' ]
    connects_down = ['|', 'F', '7', 'S']

    node = (s_x, s_y)

    moves = [
        ((-1,0), connects_to_right, connects_to_left),
        ((1,0),  connects_to_left, connects_to_right),
        ((0,-1), connects_down, connects_up),
        ((0,1),   connects_up, connects_down)]

    dist=0
    path = []
    visited = [key(s_x, s_y)]
    done = False
    while not done:
        x, y = node
        path.append(node)
        print("Checking: ", node)
        if node == (11,4):
            log = True
        else:
            log = False

        c_this_node = grid[y][x]

        if log:
            print("c_this_node", c_this_node)

        for m in moves:
            offset, valid_connects, outgoing_valid_connects = m
            new_x = x + offset[0]
            new_y = y + offset[1]

            if new_x >= 0 and new_y >= 0 and new_x < len(grid[0]) and new_y < len(grid):
                if log:
                    print(f"   {new_x}{new_y}")

                c = grid[new_y][new_x]
                if c in valid_connects and c_this_node in outgoing_valid_connects :
                    if new_x == s_x and new_y == s_y and dist > 5:
                        print("done")
                        done = True
                        break
                    elif not key(new_x,new_y) in visited:
                        node = (new_x,new_y)
                        visited.append(key(x,y))
                        dist += 1

    print(path)

    poly = Polygon(path)

    x_range = range(0, len(grid[0]))
    y_range = range(0, len(grid))

    count = 0
    for y in y_range:
        for x in x_range:
            if not key(x, y) in visited_nodes:
                point = Point(x, y)
                inside = point.within(poly)
                if inside:
                    count += 1

    plot_polygon(poly)

    print("Inside: ", count)
    #count_inside(grid, visited_nodes)

def plot_polygon(polygon):
    x, y = polygon.exterior.xy

    # Plotting
    plt.figure()
    plt.plot(x, y)
    plt.fill(x, y, alpha=0.3)  # Optional: fill the polygon with a semi-transparent color
    plt.title("Polygon Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.show()

def count_inside(grid, visited_nodes):
    x_range = range(0, len(grid[0]))
    y_range = range(0, len(grid))

    print("---- fill")
    count =0
    for y in y_range:
        for x in x_range:
            if not key(x,y) in visited_nodes:
                if not can_reach_edge(x, y, grid, visited_nodes, []):
                    print(" I ", end="")
                    count += 1
                else:
                    print(f" {grid[y][x]} ", end="")
            else:
                print(f" {grid[y][x]} ", end="")

        print()

    print("10.2 Inside count: ", count )

def can_reach_edge(x, y, grid, loop, visited):
    if x== 0 or x == len(grid[0])-1 or y == 0 or y == len(grid):
        return True
    else:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                new_x = x+dx
                new_y = y+dy
                new_key = key(new_x, new_y)
                if not new_key in loop and not new_key in visited:
                    if can_reach_edge(new_x, new_y, grid, loop, visited + [new_key]):
                        return True
    return False




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
    tiles_x = []
    tiles_y = []

    garbage_x = []
    garbage_y = []

    # Check each point in the grid

    for x in x_range:
        for y in y_range:
            if key(x,y) in visited:
                loop_points_x.append(x)
                loop_points_y.append(y)
            else:
                tiles_x.append(x)
                tiles_y.append(y)

    k = "10-4"
    print(k, k in visited )

    # Plotting
    plt.scatter(loop_points_x, loop_points_y, color='blue', label='Loop Points')  # Loop points in blue
    plt.scatter(tiles_x, tiles_y, color='red', label='Non-loop Points')  # Non-loop points in red
    plt.scatter(garbage_x, garbage_y, color='black', label='Non-loop Points')  # Non-loop points in red

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Visualization of the Loop Structure')
    plt.grid(False)  # Disables the grid

    # Inverting the y-axis
    plt.gca().invert_yaxis()

    plt.show()





part2()