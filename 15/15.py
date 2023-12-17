import time
def readfile( day):
    file_name = f"input_{day}.txt"
    string = ""
    with open(file_name, mode='r', encoding='utf-8') as f:
        while (line := f.readline()):
            string += line.strip()
    return string

def part1():
    line = readfile(15)
    grid = []

    print("line ", line)
    cmds = line.split(',')
    for c in cmds:
        print(c)

part1()
