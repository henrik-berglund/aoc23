import unittest
from approvaltests.approvals import verify
from approvaltests.reporters.generic_diff_reporter_factory import GenericDiffReporterFactory
import re

class TestWft(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        factory = GenericDiffReporterFactory()
        factory.load('myreporters.json')
        self.reporter = factory.get_first_working()
        self.char_encoding = 'iso-8859-1'


    def test_part_1(self):
        sum = 0
        with open("input.txt", mode='r', encoding='utf-8') as f:
            while (line := f.readline()):
                sum +=  self.get_num(line)

        print(sum)

    def test_part_2(self):
        sum = 0
        with open("input.txt", mode='r', encoding='utf-8') as f:
            while (line := f.readline()):
                first = self.get_first_num_2(line)
                print(f"{line} : first {first}")

    def get_num(self, str):
        match = re.search(r"\d", str)
        first = str[match.start()]
        reversed_string = ''.join(reversed(str))
        match = re.search(r"\d", reversed_string)
        last = reversed_string[match.start()]
        num = int(first + last)
        return num



    def get_last_num_2(selfself,str):
        pattern = r"(0|1|2|3|4|5|6|7|8|9|orez|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)"

    def get_first_num_2(self, str):

        pattern = r"(0|1|2|3|4|5|6|7|8|9|zero|one|two|three|four|five|six|seven|eight|nine)"
        match = re.search(pattern, str)
        matched_text = match.group()

        mapping = {
            'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
            'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
        }

        if len(matched_text) > 1:
            return mapping.get(matched_text.lower(), None)
        else:
            return int(matched_text)



if __name__ == '__main__':
    unittest.main()

