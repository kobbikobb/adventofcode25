import unittest

from day08.part2 import get_result_part_2


class TestDay08Part2(unittest.TestCase):

    def test1(self):
        test_data = """162,817,812
57,618,57
592,479,940
906,360,560
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

        result = get_result_part_2(test_data)

        self.assertEqual(25272, result)
