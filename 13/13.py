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


def sum1(grid):
    s1 = process(grid, 1)
    s2 = process(flip(grid), 100)
    return s1+s2

def flipc(c):
    if c == "#":
        return '.'
    return '#'

def sum2(grid, i):
    sumh = process3(grid, 1, i)
    sumv = process3(flip(grid), 100, i)
    return sumv + sumh

def process3(grid, mult, i):
    s1 = process2(grid)
    print(f"{i} looking for smudge ({mult})")
    new_x = 0
    found = False
    for y in range(len(grid)):
        if found:
            break
        for x in range(len(grid[0])):
            #print({y},{x},grid[y][x] )
            grid[y][x] = flipc(grid[y][x])

            s2 = process2(grid)
            if len(s2) > 1:
                s2 = s2 - s1
                new_x = list(s2)[0]
                found = True
                break
            elif len(s2) == 1 and not s1 == s2:
                new_x = list(s2)[0]
                found = True

            grid[y][x] = flipc(grid[y][x])

        if found:
            print("- found", new_x, new_x*mult)
            break
    return new_x*mult


def part2():
    lines = readfile(13)
    grid = []
    sum = 0
    gridcount=0
    for line in lines:
        if len(line) != 0:
            grid.append(list(line))
        else:
            sum += sum2(grid, gridcount)
            grid = []
            gridcount+= 1

    if len(grid) > 0:
        sum += sum2(grid, gridcount)

    print("Res 2: ", sum)
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

def process2(grid):

    lp = []
    for i, g in enumerate(grid):
        lpg = line_points(g, i)
        lp.append(lpg)
        #print("X: ", lp )

    s = set(lp[0])
    for x in lp:
        i = s.intersection(set(x))
        s = i
    return s

part2()


