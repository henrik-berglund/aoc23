def readfile( day):
    file_name = f"input_{day}.txt"
    lines = []
    with open(file_name, mode='r', encoding='utf-8') as f:
        while (line := f.readline()):
            lines.append(line.strip())
    return lines

def part1():
    lines = readfile(11)

    lines2 = []
    while len(lines) > 0:
        line = lines.pop(0)
        lines2.append(line)
        if not '#' in line:
            lines2.append(line)

    extend = []
    for col in range(len(lines2[0])):
        found = False
        for l in lines2:
            if l[col] == '#':
                found = True
        if not found:
            extend.append(col)

    extend.sort(reverse=True)
    print(extend)

    lines = []
    for l in lines2:
        ll = list(l)
        for c in extend:
            ll.insert(c,'.')
        lines.append(ll)

    coords = []
    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            if c == '#':
                coords.append((x,y))

    for c in coords:
        print(c)


part1()