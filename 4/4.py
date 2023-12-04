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

    def test_part_2(self):

        sum = 0
        cards = []
        with open("input_4.txt", mode='r', encoding='utf-8') as f:
            while (line := f.readline()):
                dummy = line.split(":")
                split2 = dummy[1].split('|')
                winning_nums =  split2[0].split(' ')
                winning_nums = [element for element in winning_nums if element != '']

                my_nums =  split2[1].strip().split(' ')
                my_nums = [element for element in my_nums if element != '']

                cards.append((dummy[0], winning_nums, my_nums))

            card_nums = []
            counts = {}
            for c in cards:
                winning_nums = c[1]
                my_nums = c[2]

                count = 0
                for n in my_nums:
                    if n in winning_nums:
                        count += 1

                card_nums.append(c[0])
                counts[c[0]] = count

            self.traverse(0, card_nums, counts)

    global card_count
    card_count = 0
    def traverse_one(self, level, card_nums, counts):
        global card_count
        c = card_nums[0]
        wins = counts[c]
        #for l in range(level):
        #    print(" ", end="")
        #print(c, ": ", wins)
        card_count += 1

        for j in range(wins):
            #print(c, "traversing child: ", j)
            self.traverse_one(level+1, card_nums[j+1:], counts)



    def traverse(self, level, card_nums, counts):
        global card_count

        for i, c in enumerate(card_nums):
            wins = counts[c]
            #for l in range(level):
            #    print(" ", end="")
            #print(c, ": ", wins)
            card_count += 1

            for j in range(wins):
                #print(c, "traversing child: ", j)
                self.traverse_one(level+1, card_nums[i+j+1:], counts)
        print("Card count: ", card_count)


if __name__ == '__main__':
    unittest.main()

