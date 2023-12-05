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
            for h in headings:
                if h in line:
                    print(line)


part1()
