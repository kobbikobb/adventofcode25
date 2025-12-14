import unittest

from day11.part1 import get_result_part_1


class TestDay11Part1(unittest.TestCase):

    def test_part_1(self):
        test_data = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""

        result = get_result_part_1(test_data)

        self.assertEqual(5, result)
