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
        part1_res = 0
        part2_res = 0

        with open("input_3.txt", mode='r', encoding='utf-8') as f:
            while (line := f.readline()):
                pass
        print(f"Day 3, part1: {part1_res}")
        print(f"Day 3, part2: {part2_res}")


if __name__ == '__main__':
    unittest.main()

