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
            #print("---Seed ", s)
            next = s
            for h in headings:
                next = lookup(next, h, maps)

            locations.append(next)
        locations.sort()
        print(locations)

def part2():
    maps = {}
    seed_ranges = []
    with open("input_5.txt", mode='r', encoding='utf-8') as f:
        while (line := f.readline()):
            if 'seeds' in line:
                nums = line[7:].split(' ')
                pairs = [int(num.strip()) for num in nums]
                while len(pairs) > 0:
                    start = pairs.pop(0)
                    l = pairs.pop(0)
                    seed_ranges.append((start, l))
            elif (match := mode_line(line)):
                mode = match
                maps[mode] = []
            elif len(line.strip()) != 0:
                tuple = line.split(' ')
                tuple = [int(num.strip()) for num in tuple]
                #print(tuple, mode)
                maps[mode].append(tuple)

        locations = []
        for s in seed_ranges:
            print("###### seed: ", s)
            next_ranges = [s]
            for h in headings:
                next_ranges = lookup_ranges(next_ranges, h, maps)

            locations.append(next_ranges)
        #locations.sort()
        locations.sort(key=lambda x : x[0] )
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

    #print(h, s, ": ", next)

    return next

def lookup_ranges(in_ranges, h, maps):
    print("*** start ", h)
    map = maps[h]
    next_ranges = []
    unmatched_in_ranges = []
    for ir in in_ranges:
        print("next in range: ", ir)
        remaining_sub_ranges_of_in_range = [ir]

        for tuple in map:
            print("tuple start: ", remaining_sub_ranges_of_in_range)
            remains_for_next_tuple = []
            while len(remaining_sub_ranges_of_in_range) > 0:
                r = remaining_sub_ranges_of_in_range.pop(0)

                t_dest, t_source, t_len = tuple
                i_start = r[0]
                i_len = r[1]

                if i_start + i_len -1 < t_source: # in is to left
                    print("left, saving for next tuple: ", r)
                    remains_for_next_tuple.append(r)
                elif i_start > t_source + t_len -1: # in is to right
                    print("right, saving for next tuple: ", r)
                    remains_for_next_tuple.append(r)
                else: #overlap
                    o_start = max(i_start, t_source)
                    o_end = min(i_start+i_len-1, t_source+t_len-1)
                    offset = t_dest-t_source
                    dest_range = (o_start+offset, o_end-o_start+1)

                    next_ranges.append(dest_range)
                    print("Overlap: ", r, ":  => ", dest_range)

                    if i_start < t_source: # remaining to left
                        rem_range = (i_start, t_source-i_start)
                        remains_for_next_tuple.append(rem_range)
                        print("left over, saving for next tuple: ", rem_range)
                    if i_start+i_len-1 > t_source + t_len -1: # remainig to right
                        rem_range = (t_source+t_len,
                                     i_start+i_len-1- t_source+t_len)
                        remains_for_next_tuple.append(rem_range)
                        print("right over, saving for next tuple: ", rem_range)

            if len(remaining_sub_ranges_of_in_range) > 0:
                print("Passed to next:", remaining_sub_ranges_of_in_range)

            remaining_sub_ranges_of_in_range = remains_for_next_tuple

        if len(remaining_sub_ranges_of_in_range) > 0:
            print("Not matched my any tuple: ", remaining_sub_ranges_of_in_range)
            unmatched_in_ranges.extend(remaining_sub_ranges_of_in_range)

    if len(unmatched_in_ranges) > 0:
        print("Unmatched:",unmatched_in_ranges )
        next_ranges.extend(unmatched_in_ranges)

    print(h, ": ", in_ranges, " => ", next_ranges)
    return next_ranges

part2()
