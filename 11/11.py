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

    sum = 0
    for i, c1 in enumerate(coords):
        for c2 in coords[i+1:]:
            xd = abs(c1[0]-c2[0])
            yd = abs(c1[1]-c2[1])
            dist = xd+yd
            sum += dist
            print(f"From {c1} to {c2} = {xd} {yd}")

    print("Part 1", sum)

def part2():
    lines = readfile(11)

    coords = []
    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            if c == '#':
                coords.append((x,y))

    print(coords)

    y_add = []
    for y, l in enumerate(lines):
        if not '#' in l:
            y_add.append(y)
    print(y_add)

    to_add = 999999
    c2 = []
    for c in coords:
        x,y = c
        a = 0
        for ya in y_add:
            if y > ya:
                a+= 1
        c2.append((x, y+a*to_add))

    print()
    print("c2: ", c2)

    x_add = []
    for x in range(len(lines[0])):
        ext = True
        for y, l in enumerate(lines):
            if l[x] == '#':
                ext = False
        if ext:
            x_add.append(x)

    print("xa", x_add)

    c3 = []
    for c in c2:
        x,y = c
        a = 0
        for xa in x_add:
            if x > xa:
                a+= 1
        c3.append((x+a*to_add, y))
    print(c3)

    coords = c3
    sum = 0
    for i, c1 in enumerate(coords):
        for c2 in coords[i+1:]:
            xd = abs(c1[0]-c2[0])
            yd = abs(c1[1]-c2[1])
            dist = xd+yd
            sum += dist
            print(f"From {c1} to {c2} = {xd} {yd}")

    print("Part 2", sum)


part2()