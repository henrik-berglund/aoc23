import time
def readfile( day):
    file_name = f"input_{day}.txt"
    string = ""
    with open(file_name, mode='r', encoding='utf-8') as f:
        while (line := f.readline()):
            string += line.strip()
    return string

def hash(str):
    cur = 0
    for c in str:
        a = ord(c)
        cur += a
        cur *= 17
        cur = cur % 256
    return cur

def part1():
    line = readfile(15)
    sum = 0

    print("line ", line)
    cmds = line.split(',')
    for c in cmds:
        sum += hash(c)

    print("Part 16.1: ", sum)

def parse(cmd):
    i = 0
    label = ""
    while cmd[i] != '=' and cmd[i] != '-':
        label += cmd[i]
        i+= 1

    op = cmd[i]
    i+= 1

    box = hash(label)
    val = None
    if op == '=':
        val = int(cmd[i:])

    return box, label, op, val


def perform_op(box, label_in, op_in, val):
    new_box = []
    found = False
    for l in box:
        label, len = l
        if label == label_in:
            found = True
            if op_in == '=':
                new_box.append((label_in, val))
        else:
            new_box.append(l)

    if not found and op_in == '=':
        new_box.append((label_in, val))

    return new_box

def focalp(box, boxno):
    sum = 0
    for j, l in enumerate(box):
        label, val = l
        s= (boxno+1) * (j+1) * val
        sum += s
        print(f"{label} {s}")
    return sum

def part2():
    line = readfile(15)
    boxes = []
    for i in range(256):
        boxes.append(list())

    print("line ", line)
    cmds = line.split(',')
    for c in cmds:
        box, label, op, val = parse(c)
        print(c)
        print(f" {box},{label},{op},{val}")
        boxes[box] = perform_op(boxes[box], label, op, val)

    sum = 0
    for i, box in enumerate(boxes):
        if len(box) > 0:
            print(f"{i}, {box}")
            sum += focalp(box, i)

    print("15.2: ", sum)

part2()
