import unittest

from day06.part1 import get_result_part_1


class TestDay06Part1(unittest.TestCase):

    def test1(self):
        test_data = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +"""

        result = get_result_part_1(test_data)

        self.assertEqual(4277556, result)
