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
        day =8
        map = {}
        file = self.readfile(day)
        for line in file:
            if '=' in line:
                node_def = line.split("=")
                start = node_def[0].strip()
                dirs = node_def[1].strip()[1:-1]
                lr = dirs.split(",")
                left = lr[0].strip()
                right = lr[1].strip()
                map[start] = (left, right)
            elif len(line) != 0:
                dirs = list(line)
                print(f"dirs: {dirs}")

        for k in map.keys():
            print(f"{k}: {map[k][0]} {map[k][1]}")
#        print(f"Day {day}, part1: {part1_res}")


if __name__ == '__main__':
    unittest.main()

