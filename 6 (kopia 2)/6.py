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
                lines.append(line)
        return lines

    def test_util(self):
        verify("hej", self.reporter)

    def test_part_1(self):
        day =6
        part1_res = 0
        file = self.readfile(day)
        for line in file:
            pass

        print(f"Day {day}, part1: {part1_res}")


if __name__ == '__main__':
    unittest.main()

