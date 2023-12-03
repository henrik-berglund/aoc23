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

    def add_coords(self, coord, delta):
        return (coord[0]+delta[0], coord[1]+delta[1])

    def test_part_2(self):
        nc = self.get_numbers_and_coords()

        sc, stars = self.get_symbols()
        sum = 0

        deltas = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1,1), (0, 1), (-1,1)]

        for star_c in stars:
            print(f"* : {star_c}")
            count=0
            gear = 1
            found = False
            for num in nc:
                number, num_c = num
                for d in deltas:
                    c = self.add_coords(star_c, d)
                    if c in num_c:
                        found = True
                        count += 1
                        gear *= number
                        print(f"  {c} is in {num_c}: num {number}, count: {count}")
                        break
            if count == 2:
                print(f"**Adding: {gear}")
                sum += gear

        print(f"3.2, Sum: {sum}")

    def test_part_1(self):
        nc = self.get_numbers_and_coords()

        sc, stars = self.get_symbols()
        sum = 0

        deltas = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1,1), (0, 1), (-1,1)]
        for num in nc:
            found = False
            number, num_coords = num

            for nc in num_coords:

                for d in deltas:
                    c = self.add_coords(nc, d)
                    if c in sc:
                        found = True
                        break
                if found:
                    break

            if found:
                sum += number

        print(f"3.1, Sum: {sum}")
    def get_symbols(self):
        symbols = []
        stars = []

        with open("input_3.txt", mode='r', encoding='utf-8') as f:
            line_no=0
            num = ""
            coordinates = []
            while (line := f.readline()):
                for x, c in enumerate(line):
                    if not c.isdigit() and c != '.' and c != '\n':
                        symbols.append((x, line_no))
                        if c == '*':
                            stars.append((x, line_no))
                line_no += 1
            return symbols, stars

    def get_numbers_and_coords(self):
        numbers = []
        with open("input_3.txt", mode='r', encoding='utf-8') as f:
            line_no=0
            num = ""
            coordinates = []
            while (line := f.readline()):
                for x, c in enumerate(line):
                    if c.isdigit():
                        num += c
                        coordinates.append((x, line_no))
                    elif num.isdigit():
                        numbers.append((int(num), coordinates))
                        num = ""
                        coordinates = []
                line_no += 1
            return numbers


if __name__ == '__main__':
    unittest.main()

