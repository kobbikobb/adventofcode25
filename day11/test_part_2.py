import unittest

from day11.part2 import get_result_part_2


class TestDay11Part2(unittest.TestCase):

    def test_part_1(self):
        test_data = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""

        result = get_result_part_2(test_data)

        self.assertEqual(2, result)
