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
        day =9
        in_nums = []
        file = self.readfile(day)
        for line in file:
            strs = line.split(' ')
            nums = [int(n) for n in strs]
            in_nums.append(nums)
            pass

        sum_1 = 0
        for n in in_nums:
            print("-------")
            print("line: ", n)
            seq = []
            seq.append(n)
            while not all_zero(seq[-1]):
                new = self.new_seq(seq[-1])
                seq.append(new)

            for s in seq:
                print(s)
            self.predict(seq)

            pred = seq[0][-1]
            sum_1 += pred
            print("pred: ", pred)

        print("Res: ", sum_1)

    def predict(self, seq):
        print("predict-----")
        i = len(seq)-1
        prev_last=0
        while  i>= 0:
            s = seq[i]
            last = s[-1]
            s.append(last+ prev_last)
            prev_last = s[-1]
            i -= 1
            print(s)

    #fel Res:  1757008038
    

    def new_seq(self,seq):
        s = []
        for i in range(1,len(seq)):
            s.append(seq[i]- seq[i-1])
        return s

        #print(f"Day {day}, part1: {part1_res}")


def all_zero(s):
    for i in s:
        if i != 0:
            return False
    return True

if __name__ == '__main__':
    unittest.main()

