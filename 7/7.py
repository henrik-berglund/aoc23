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

    def four(self, hand):
        vals = {}
        for h in hand:
            vals[h] = True

        return len(vals.keys() == 2)

    def five(self, hand):
        val = hand[0]
        for v in hand:
            if v != val:
                return False
        return True

    def get_rank(self, hand):
        if self.five(hand):
            return 1
        elif self.four(hand):
            return 2

        return None

    def test_part_1(self):
        day = 7

        hands = []
        file = self.readfile(day)
        for line in file:
            items = line.split(' ')
            rank = self.get_rank(items[0])
            hand = (items[0], int(items[1]), rank)
            print(hand)
            hands.append(hand)

#        print(f"Day {day}, part1: {part1_res}")


if __name__ == '__main__':
    unittest.main()

