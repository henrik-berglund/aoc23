import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon

import time
def readfile( day):
    file_name = f"input_{day}.txt"
    lines = []
    with open(file_name, mode='r', encoding='utf-8') as f:
        while (line := f.readline()):
            lines.append(line.strip())
    return lines


def part1():
    lines = readfile(18)
    instr = []
    for line in lines:
        s1 = line.split(" ")
        instr.append((s1[0], int(s1[1]), s1[2][1:-1]))

    coords = [(0,0)]
    x = 0
    y = 0
    dir = {'R': (1,0), 'U' : (0,-1), 'D': (0,1), 'L': (-1,0)}
    for i in instr:
        d, l, col = i
        dx, dy = dir[d]
        for j in range(l):
            x += dx
            y += dy
            coords.append((x,y))


    max_x =0
    max_y = 0
    min_x = 999
    min_y = 999

    for c in coords:

        x,y = c
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

        if y < min_y:
            min_y = y

        if x < min_x:
            min_x = x

    width = max_x - min_x + 1
    height = max_y- min_y + 1

    print(min_x, min_y, max_x, max_y)

    #grid = []
    #for y in range(height):
    #    grid.append(list('.'*width))

#    for c in coords:
##        x, y = c
  #      x -= min_x
   #     y -= min_y
        #print(x, y)
    #    grid[y][x] = '#'

    count=0
    poly = Polygon(coords)
    #plot_polygon(poly)
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            point = Point(x, y)
            inside = point.within(poly)
            if inside:
                count += 1

    print("18.1: ", count + len(coords)-1)
    print("Poly area", poly.area)

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

part1()

