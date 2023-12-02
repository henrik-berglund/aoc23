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
        with open("input_2.txt", mode='r', encoding='utf-8') as f:
            while (line := f.readline()):
                parts = line.split(':', maxsplit=1)
                num = int(parts[0].split(' ', maxsplit=1)[1])
                print(f"num {num}: {line}")

if __name__ == '__main__':
    unittest.main()

