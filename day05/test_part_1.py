import unittest

from day05.part1 import get_result_part_1


class TestDay05Part1(unittest.TestCase):

    def test1(self):
        test_data = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

        result = get_result_part_1(test_data)

        self.assertEqual(3, result)
