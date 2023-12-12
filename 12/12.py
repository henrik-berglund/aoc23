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

    cparts = []
    for p in parts:
        line = []
        dcount =0
        for c in p[0]:
            if c == '#':
                dcount += 1
            elif dcount != 0:
                line.append(('d', dcount))
                dcount=0

                line.append(c)
            else:
                line.append(c)

        if dcount != 0:
            line.append(('d', dcount))
            dcount = 0

        cparts.append(line)


        for i, p in enumerate(cparts):
            print(f"{lines[i]}\n***{p}\n")


part1()