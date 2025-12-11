import unittest

from day09.part1 import get_result_part_1, size_between_corners


class TestDay08Part1(unittest.TestCase):

    def test_calculate_size_between_corners_1(self):
        corner_a = (2, 5)
        corner_b = (9, 7)

        result = size_between_corners(corner_a, corner_b)

        self.assertEqual(24, result)

    def test_calculate_size_between_corners_2(self):
        corner_a = (7, 1)
        corner_b = (11, 7)

        result = size_between_corners(corner_a, corner_b)

        self.assertEqual(35, result)

    def test_calculate_size_between_corners_3(self):
        corner_a = (7, 3)
        corner_b = (2, 3)

        result = size_between_corners(corner_a, corner_b)

        self.assertEqual(6, result)

    def test_part_1(self):
        test_data = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

        result = get_result_part_1(test_data)

        self.assertEqual(50, result)
