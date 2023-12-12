def readfile( day):
    file_name = f"input_{day}.txt"
    lines = []
    with open(file_name, mode='r', encoding='utf-8') as f:
        while (line := f.readline()):
            lines.append(line.strip())
    return lines

def part1():
    lines = readfile(12)
    parts = []
    for line in lines:
        p, c = line.split(" ")
        c = c.split(",")
        counts = [int(n) for n in c]
        parts.append((p,counts))

    for p in parts:
        print(p)


part1()