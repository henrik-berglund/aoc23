import unittest
from approvaltests.approvals import verify
from approvaltests.reporters.generic_diff_reporter_factory import GenericDiffReporterFactory
import re
from collections import Counter

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
        counts = Counter(hand)

        if len(counts.keys()) == 2:
            c = [counts[x] for x in counts.keys()]
            c.sort(reverse=True)
            #print(c)
            return c[0] == 4
        return False

    def full(self, hand):
        counts = Counter(hand)

        if len(counts.keys()) == 2:
            c = [counts[x] for x in counts.keys()]
            c.sort(reverse=True)
            #print(c)
            return c[0] == 3
        return False

    def three(self, hand):
        counts = Counter(hand)

        if len(counts.keys()) == 3:
            c = [counts[x] for x in counts.keys()]
            c.sort(reverse=True)
            #print(c)
            return c[0] == 3
        return False

    def twop(self, hand):
        counts = Counter(hand)

        if len(counts.keys()) == 3:
            c = [counts[x] for x in counts.keys()]
            c.sort(reverse=True)
            #print(c)
            return c[0] == 2 and c[1] == 2
        return False

    def onep(self, hand):
        counts = Counter(hand)

        if len(counts.keys()) == 4:
            c = [counts[x] for x in counts.keys()]
            c.sort(reverse=True)
            #print(c)
            return c[0] == 2
        return False

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
        elif self.full(hand):
            return 3
        elif self.three(hand):
            return 4
        elif self.twop(hand):
            return 5
        elif self.onep(hand):
            return 6
        else:
            return 7

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

