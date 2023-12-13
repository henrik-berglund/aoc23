def readfile( day):
    file_name = f"input_{day}.txt"
    lines = []
    with open(file_name, mode='r', encoding='utf-8') as f:
        while (line := f.readline()):
            lines.append(line.strip())
    return lines


def part1():
    lines = readfile(13)
    grid = []
    sum = 0
    for line in lines:
        if len(line) ==0:
            sum += process(grid)
            grid = []
        else:
            grid.append(line)

    if len(grid) > 0:
        sum+= process(grid)

    print("Res 1: ", sum)
def line_points(line):
    xpoints = []

    for x in range (1, len(line)-2):
        match = x
        for diff in range(len(line)):
            lx = x+1-(diff)
            rx = x+diff
            if lx >= 0 and rx < len(line) :
                if line[lx] != line[rx]:
                    match=None
        if match:
            xpoints.append(match)

    return xpoints

def process(grid):
    print("-----")

    for g in grid:
        print(g)

    lp = []
    for g in grid:
        lp.append(line_points(g))
        print("X: ", line_points(g) )

    s = set(lp[0])
    for x in lp:
        i = s.intersection(x)
        s = i
    print(s)
    res = 0
    if len(s) >0:
        res =  list(s)[0]
    print (res)
    return res

part1()