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
        with open("input_4.txt", mode='r', encoding='utf-8') as f:
            while (line := f.readline()):
                dummy = line.split(":")
                split2 = dummy[1].split('|')
                winning_nums =  split2[0].split(' ')
                winning_nums = [element for element in winning_nums if element != '']

                my_nums =  split2[1].strip().split(' ')
                my_nums = [element for element in my_nums if element != '']

                value = 0
                for n in my_nums:
                    if n in winning_nums:
                        if value == 0:
                            value = 1
                        else:
                            value *= 2
                sum += value

                print("*", winning_nums)
                print("+", my_nums)
                print(":", value)

        print(f"Day 3, part1: {sum}")
        #print(f"Day 3, part2: {part2_res}")


if __name__ == '__main__':
    unittest.main()

