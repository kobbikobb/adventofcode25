import unittest

from day02.part2 import get_result_part_2


class TestDay02Part2(unittest.TestCase):
    def test1(self):
        test_data = """11-22"""

        result = get_result_part_2(test_data)

        self.assertEqual(33, result)

    def test2(self):
        test_data = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""

        result = get_result_part_2(test_data)

        self.assertEqual(4174379265, result)
