def readfile( day):
    file_name = f"input_{day}.txt"
    lines = []
    with open(file_name, mode='r', encoding='utf-8') as f:
        while (line := f.readline()):
            lines.append(line.strip())
    return lines

def dropn(grid):
    for x in range(len(grid[0])):
        for y in range(1,len(grid)):
            if grid[y][x] == 'O':
                dy = y
                while dy > 0 and grid[dy-1][x] == '.':
                    grid[dy][x] = '.'
                    grid[dy-1][x] = 'O'
                    dy -= 1

def clockw(grid):
    g2 = []
    for l in grid[0]:
        g2.append(list('Q'*len(grid)))
    rows_in = len(grid)
    cols_in = len(grid[0])

    for l in range(rows_in):
        for c in range(cols_in):
            #g2[rows_in-1-c][l] = grid[l][c]
            g2[l][c] = grid[rows_in-1-c][l]

    return g2

def part1():
    lines = readfile(14)
    grid = []
    for line in lines:
        if len(line) != 0:
            grid.append(list(line))

    for line in grid:
        print(line)

    print("------- drop")
    dropn(grid)
    for line in grid:
        print(line)

    print("------- clockw")
    grid = clockw(grid)
    for line in grid:
        print(line)
    exit(0)
    sum = 0
    num = len(grid)
    for line in grid:
        sum+= line.count('O') *num
        print(line, num, line.count('O'))
        num -= 1

    print("Part 14.1: ", sum
          )
part1()