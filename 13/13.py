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
    for line in lines:
        if len(line) ==0:
            process(grid)
            grid = []
        else:
            grid.append(line)

    if len(grid) > 0
        process(grid)

def process(grid):
    print("-----")
    line = grid[0]

    for x in range (1, len(line)-2):
        match = x
        for diff in range(len(line)):
            lx = x-diff
            rx = x+diff
            if lx >= 0 and rx < len(line) :
                if line(lx) != line(rx):
                    match=None
        if match:
            break

    for g in grid:
        print(g)
    print("X: ", match)
    return match


part1()