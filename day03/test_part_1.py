import unittest

from day03.part1 import get_result_part_1


class TestDay03Part1(unittest.TestCase):

    def test1(self):
        test_data = """811111111111119"""

        result = get_result_part_1(test_data)

        self.assertEqual(89, result)

    def test2(self):
        test_data = """987654321111111"""

        result = get_result_part_1(test_data)

        self.assertEqual(98, result)

    def test3(self):
        test_data = """234234234234278"""

        result = get_result_part_1(test_data)

        self.assertEqual(78, result)

    def test4(self):
        test_data = """818181911112111"""

        result = get_result_part_1(test_data)

        self.assertEqual(92, result)

    def test5(self):
        test_data = """987654321111111
811111111111119
234234234234278
818181911112111"""

        result = get_result_part_1(test_data)

        self.assertEqual(357, result)


if __name__ == "__main__":
    unittest.main()
