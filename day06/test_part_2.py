import unittest

from day06.part2 import get_result_part_2


class TestDay06Part2(unittest.TestCase):



    def test1(self):
        test_data = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +"""

        result = get_result_part_2(test_data)

        self.assertEqual(3263827, result)
