headings = ['seed-to-soil',
            'soil-to-fertilizer',
            'fertilizer-to-water',
            'water-to-light',
            'light-to-temperature',
            'temperature-to-humidity',
            'humidity-to-location' ]

def mode_line(line):
    mode = None
    for h in headings:
        if h in line:
            mode = h
    return mode

def part1():
    maps = {}

    with open("input_5.txt", mode='r', encoding='utf-8') as f:
        while (line := f.readline()):
            if 'seeds' in line:
                nums = line[7:].split(' ')
                seeds = [int(num.strip()) for num in nums]
                #print(seeds)
            elif (match := mode_line(line)):
                mode = match
                #print("mode: ", mode)
                maps[mode] = []
            elif len(line.strip()) != 0:
                tuple = line.split(' ')
                tuple = [int(num.strip()) for num in tuple]
                #print(tuple, mode)
                maps[mode].append(tuple)

        locations = []
        for s in seeds:
            print("---Seed ", s)
            next = s
            for h in headings:
                next = lookup(next, h, maps)

            locations.append(next)
        locations.sort()
        print(locations)



def lookup(s, h, maps):
    map = maps[h]
    next = None
    for tuple in map:
        dest, source, len = tuple
        if s >= source and s < source+len:
            next = dest + s - source
    if not next:
        next = s

    print(h, s, ": ", next)

    return next

part1()
