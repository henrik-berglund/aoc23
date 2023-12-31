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
    maxq = 0
    for line in lines:
        p, c = line.split(" ")
        print(p)
        qcount = p.count("?")
        if maxq < qcount:
            maxq = qcount
        c = c.split(",")
        counts = [int(n) for n in c]
        parts.append((p,counts))
    print("Max q: ", maxq)
    cparts = []
    for p in parts:
        line = []
        count = 0
        last = None
        for c in p[0]:
            if last and c == last:
                count += 1
            elif last and c != last:
                line.append((last, count))
                count = 1
                last = c
            else:
                last = c
                count = 1

        if count != 0:
            line.append((last, count))
            count = 0

        cparts.append((line, p[1]))


        for i in range(len(cparts)):
            print(f"{lines[i]}")
            cp = cparts[i]
            print("cp ", cp)
            parts = cp[0]
            counts = cp[1]
            print("parts: ", parts)
            print(f"counts: {counts}\n")

            cparts[i] = reduce_cpart(cparts[i])


def reduce_cpart(p):
    parts = p[0]
    counts = p[1]
    print("parts: ", parts)
    print(f"counts: {counts}\n")

    found = False
    c1 = counts[0]
    for x, p in enumerate(parts):
        if p[0] == '#' and p[1] == c1:
            print("=>> First # group matches as is")
            new_parts = parts[x + 1:]
            new_counts = counts[1:]
            return (new_parts, new_counts)
    return p

part1()