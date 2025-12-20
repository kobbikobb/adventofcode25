import unittest

from day12.part1 import get_result_part_1


class TestDay12Part1(unittest.TestCase):
    """Test for day 12 part 1"""

    def test_part_1(self):
        test_data = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""

        result = get_result_part_1(test_data)

        self.assertEqual(2, result)
