import unittest

from day09.part2 import get_result_part_2


class TestDay09Part2(unittest.TestCase):

    def test_part_1(self):
        test_data = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

        result = get_result_part_2(test_data)

        self.assertEqual(24, result)
