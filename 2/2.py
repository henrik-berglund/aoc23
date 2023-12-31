import unittest
from approvaltests.approvals import verify
from approvaltests.reporters.generic_diff_reporter_factory import GenericDiffReporterFactory
import re

class TestWft(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        #factory = GenericDiffReporterFactory()
        #factory.load('myreporters.json')
        #self.reporter = factory.get_first_working()
        #self.char_encoding = 'iso-8859-1'
        pass

    def test_part_1(self):
        sum = 0
        power_sum = 0
        with open("input_2.txt", mode='r', encoding='utf-8') as f:
            while (line := f.readline()):
                parts = line.split(':', maxsplit=1)
                game_no = int(parts[0].split(' ', maxsplit=1)[1])
                print(f"{game_no}: {line}")
                max = {}

                max['blue'] = 0
                max['green'] = 0
                max['red'] = 0

                parts = parts[1].split(';')
                for p in parts:
                    print(f"  {p}")
                    cubes = p.strip().split(',')
                    for c in cubes:
                        cube_def = c.strip().split(' ')
                        #print(f"    cube_def:{cube_def}")

                        no_of_cubes = int(cube_def[0])
                        cube_col = cube_def[1]
                        #print(f"    {cube_col}:{no_of_cubes}")

                        if no_of_cubes > max[cube_col]:
                            max[cube_col] = no_of_cubes


                print(f"max: {max}")


                if  max['blue'] <= 14 and max['red'] <= 12 and max['green'] <= 13:
                    sum += game_no
                power_sum +=  max['blue'] * max['red'] * max['green']

        print(f"Day 2, part1: {sum}")
        print(f"Day 2, part2: {power_sum}")


if __name__ == '__main__':
    unittest.main()

