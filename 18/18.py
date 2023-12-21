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

    for i in instr:
        print (i)

    #for line in grid:
    #    print(line)

part1()

