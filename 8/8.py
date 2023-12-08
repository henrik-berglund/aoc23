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

    def _test_part_1(self):
        day =8
        map = {}
        file = self.readfile(day)
        for i, line in enumerate(file):
            if '=' in line:
                node_def = line.split("=")
                start = node_def[0].strip()
                d = node_def[1].strip()[1:-1]
                lr = d.split(",")
                left = lr[0].strip()
                right = lr[1].strip()
                map[start] = (left, right, i)
            elif len(line) != 0:
                dirs = list(line)
                print(f"dirs: {dirs}")

        key = 'AAA'
        steps = 0
        pos = 0
        print(dirs)
        while key != 'ZZZ':
            dir = dirs[pos]

            if dir == 'L':
                key2 = map[key][0]
            else:
                key2 = map[key][1]
            print(f"{key}+{dir} => {key2}")
            key=key2

            steps += 1
            pos += 1
            if pos == len(dirs):
                pos=0

        print(f"Day {day}, part1: {steps}")

    def test_part_2(self):
        day =8
        map = {}
        file = self.readfile(day)
        for i, line in enumerate(file):
            if '=' in line:
                node_def = line.split("=")
                start = node_def[0].strip()
                d = node_def[1].strip()[1:-1]
                lr = d.split(",")
                left = lr[0].strip()
                right = lr[1].strip()
                map[start] = (left, right, i)
            elif len(line) != 0:
                dirs = list(line)
                #print(f"dirs: {dirs}")

        start_keys = []
        for k in map.keys():
            if list(k)[2] == 'A':
                start_keys.append(k)
        print("start_keys: ", start_keys)

        steps = 0
        pos = 0
        #print(dirs)
        used_rules = set()
        while not all_z(start_keys):
            dir = dirs[pos]
            #print(f"{dir}:{start_keys}")

            new_keys = []
            rules = ""
            for k in start_keys:
                if dir == 'L':
                    key2 = map[k][0]
                else:
                    key2 = map[k][1]
                new_keys.append(key2)
                rules += "-"+str(map[k][2])

            if rules in used_rules:
                print("Loop: ", used_rules)
                exit(1)
            used_rules.add(rules)

            #print(f"{dir}+{start_keys} => {new_keys} rules {rules}")
            start_keys = new_keys
            steps += 1
            pos += 1
            if pos == len(dirs):
                pos=0
                #print("-------- wrap of dirs")

        print(f"Day {day}, part2: {steps}")

def all_z(keys):
    for k in keys:
        if k[2] != 'Z':
            return False
    return True

if __name__ == '__main__':
    unittest.main()

