def readfile( day):
    file_name = f"input_{day}.txt"
    lines = []
    with open(file_name, mode='r', encoding='utf-8') as f:
        while (line := f.readline()):
            lines.append(line.strip())
    return lines

def flip(grid):
    flipped = []

    for x in grid[0]:
        flipped.append(list(' '*len(grid)))

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            flipped[x][y] = grid[y][x]
    return flipped

def part1():
    lines = readfile(13)
    grid = []
    sum = 0
    for line in lines:
        if len(line) == 0:

            s1 = process(grid, 1)
            s2  = process(flip(grid), 100)
            sum += s1+s2
            grid = []
        else:
            grid.append(list(line))

    if len(grid) > 0:
        s1 = process(grid, 1)
        s2 = process(flip(grid), 100)

        sum += s1 + s2

    print("Res 1: ", sum)


def sum1(grid):
    s1 = process(grid, 1)
    s2 = process(flip(grid), 100)
    return s1+s2

def part2():
    lines = readfile(13)
    grid = []
    sum = 0
    for line in lines:
        if len(line) == 0:
            sum += sum1(grid)
            grid = []
        else:
            grid.append(list(line))

    if len(grid) > 0:
        sum += sum1(grid)

    print("Res 1: ", sum)
def line_points(line, no):
    xpoints = []
    #print(f"\nChecking {no}", line)

    for x in range (1, len(line)):
        s1 = line[0:x]
        s2 = line[x:]
        s1 = list(reversed(s1))
        #print(f"-- {x} s1r: {s1}\n-- s2: {s2}")

        match=True
        index = 0
        while index < len(s1) and index < len(s2):
            if s1[index] != s2[index]:
                match=False
                break
            index+=1

        if match:
            xpoints.append(x)
    #print("==>", xpoints)
    return xpoints

def process(grid, mult):

    lp = []
    for i, g in enumerate(grid):
        lpg = line_points(g, i)
        lp.append(lpg)
        #print("X: ", lp )

    s = set(lp[0])
    for x in lp:
        i = s.intersection(set(x))
        s = i
    #print(s)
    res = 0
    if len(s) >0:
        res =  list(s)[0]

    #print (res*mult)
    return res*mult

part1()
part2()


