import unittest

from day01.solution import get_hits_part_1


class TestDay01Part1(unittest.TestCase):

    def test1(self):
        test_data = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

        result = get_hits_part_1(test_data)

        self.assertEqual(3, result)

    def test2(self):
        test_data = """L50
L10
L90
L5
R5
R3
R3
L6"""

        result = get_hits_part_1(test_data)

        self.assertEqual(4, result)

    def test3(self):
        test_data = """R50
R1
R2
R1
L4"""

        result = get_hits_part_1(test_data)

        self.assertEqual(2, result)

    def test4(self):
        test_data = """L250"""

        result = get_hits_part_1(test_data)

        self.assertEqual(1, result)


if __name__ == "__main__":
    unittest.main()
