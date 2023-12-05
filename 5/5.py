headings = ['seeds',
            'seed-to-soil',
            'soil-to-fertilizer',
            'fertilizer-to-water',
            'water-to-light',
            'light-to-temperature',
            'temperature-to-humidity',
            'humidity-to-location map' ]

def part1():
    with open("input_5.txt", mode='r', encoding='utf-8') as f:
        while (line := f.readline()):
            if 'seeds' in line:
                nums = line[:5]
                print(nums)
            else:
                for h in headings:
                    print(line)


part1()
