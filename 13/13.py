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
    if len(grid) > 0:
        process(grid)

def process(grid):
    print("-----")
    for g in grid:
        print(g)

part1()