import unittest

from day05.part2 import get_result_part_2


class TestDay05Part2(unittest.TestCase):

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

        result = get_result_part_2(test_data)

        self.assertEqual(14, result)
