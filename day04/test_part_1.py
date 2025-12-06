import unittest

from day04.part1 import get_result_part_1


class TestDay04Part1(unittest.TestCase):

    def test1(self):
        test_data = """..@@.@@@@."""

        result = get_result_part_1(test_data)

        self.assertEqual(6, result)

    def test2(self):
        test_data = """..@@.@@@@.
@@@@..@.@@"""

        #..@x.xx@x.
        #xx@x..x.xx

        result = get_result_part_1(test_data)

        self.assertEqual(10, result)

    def test3(self):
        test_data = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

        result = get_result_part_1(test_data)

        self.assertEqual(13, result)


if __name__ == "__main__":
    unittest.main()
