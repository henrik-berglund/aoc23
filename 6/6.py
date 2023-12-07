import unittest
from approvaltests.approvals import verify
from approvaltests.reporters.generic_diff_reporter_factory import GenericDiffReporterFactory
import re

class TestAoc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        factory = GenericDiffReporterFactory()
        factory.load('myreporters.json')
        self.reporter = factory.get_first_working()
        self.char_encoding = 'iso-8859-1'
        pass

    def readfile(self, day):
        file_name = f"input_{day}.txt"
        lines = []
        with open(file_name, mode='r', encoding='utf-8') as f:
            while (line := f.readline()):
                lines.append(line.strip())
        return lines

    def test_util(self):
        verify("hej", self.reporter)

    def test_part_1(self):
        day =6
        part1_res = 1

        #races = [(7, 9), (15, 40), (30, 200)]
        races = [(35, 213),(69,1168),(68, 1086), (87, 1248)]

        for i, r in enumerate(races):
            time = r[0]
            record = r[1]
            race_wins = 0
            for charge in range(time+1):
                dist = (time-charge)*charge
                #print(f"{i} {charge}s, race {time-charge} dist {dist}")
                if dist > record:
                    race_wins += 1
            part1_res *= race_wins

        print(f"Day {day}, part1: {part1_res}")

    def test_part_1(self):
        day =6
        part1_res = 1

        time = 35696887
        record = 213116810861248
        race_wins = 0
        for charge in range(time+1):
            dist = (time-charge)*charge
            if charge % 1000000 == 0:
                print(".", end="", flush=True)
            if dist > record:
                race_wins += 1

        print(f"Day {day}, part2: {race_wins}")

if __name__ == '__main__':
    unittest.main()

