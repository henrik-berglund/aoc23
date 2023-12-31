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

    def rank(self, letter):
        letters = 'AKQJT98765432'
        num = letters.find(letter)+1
        return hex(num)[2:]

    def rank2(self, letter):
        letters = 'AKQT98765432J'
        num = letters.find(letter)+1
        return hex(num)[2:]

    def secondary_rank(self, hand):
        str = ""
        for h in hand:
            str += self.rank(h)
        return str

    def secondary_rank2(self, hand):
        str = ""
        for h in hand:
            str += self.rank2(h)
        return str

    def get_main_rank(self, hand):
        variants = 'AKQT98765432'

        letters = list(hand)
        if 'J' in letters:
            min_rank = "888888"
            index = letters.index('J')
            print(index, ": ", letters)
            for v in variants:
                letters[index] = v
                new = "".join(letters)
                new_rank = self.get_main_rank(new)
                if new_rank < min_rank:
                    min_rank = new_rank
                print("---", new, ": ", min_rank)

            return min_rank


        if self.five(hand):
            return "1"
        elif self.four(hand):
            return "2"
        elif self.full(hand):
            return "3"
        elif self.three(hand):
            return "4"
        elif self.twop(hand):
            return "5"
        elif self.onep(hand):
            return "6"
        else:
            return "7"

        return None

    def test_part_1(self):
        day = 7

        hands = []
        file = self.readfile(day)
        for line in file:
            items = line.split(' ')
            rank = self.get_main_rank(items[0])+self.secondary_rank2(items[0])
            hand = (items[0], int(items[1]), rank)
            hands.append(hand)

        hands.sort(key = lambda x : x[2], reverse=True)
        wins = 0
        for i, h in enumerate(hands):
            print(h)
            rank = i+1
            bid = h[1]
            win = rank*bid
            wins += win
        print(f"Day {day}, part1: {wins}")


if __name__ == '__main__':
    unittest.main()

