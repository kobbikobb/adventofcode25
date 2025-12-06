import unittest

from day04.part2 import get_result_part_2


class TestDay04Part2(unittest.TestCase):

    def test1(self):
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

        result = get_result_part_2(test_data)

        self.assertEqual(43, result)


if __name__ == "__main__":
    unittest.main()
