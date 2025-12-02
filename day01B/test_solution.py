import unittest
from day02.solution import get_hit


class TestDay01(unittest.TestCase):


    def test1(self):
        self.test_data = """L51"""

        result = get_hit(self.test_data)

        self.assertEqual(1, result)

    def test2(self):
        self.test_data = """L51
L2
R3"""

        result = get_hit(self.test_data)

        self.assertEqual(2, result)

    def test3(self):
        self.test_data = """L51
R1
R1
L1
R1"""

        result = get_hit(self.test_data)

        self.assertEqual(3, result)

    def test4(self):
        self.test_data = """R300"""

        result = get_hit(self.test_data)

        self.assertEqual(3, result)

    def test5(self):
        self.test_data = """L300"""

        result = get_hit(self.test_data)

        self.assertEqual(3, result)

    def test6(self):
        self.test_data = """R1000"""

        result = get_hit(self.test_data)

        self.assertEqual(10, result)

    def test7(self):
        self.test_data = """L1000"""

        result = get_hit(self.test_data)

        self.assertEqual(10, result)

    def test8(self):
        self.test_data = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

        result = get_hit(self.test_data)

        self.assertEqual(6, result)

    def test9(self):
        self.test_data = """L150"""

        result = get_hit(self.test_data)

        self.assertEqual(2, result)

    def test10(self):
        self.test_data = """R150"""

        result = get_hit(self.test_data)

        self.assertEqual(2, result)

    def test11(self):
        self.test_data = """R40
R105"""

        result = get_hit(self.test_data)

        self.assertEqual(1, result)

    def test12(self):
        self.test_data = """L40
L105"""

        result = get_hit(self.test_data)

        self.assertEqual(1, result)

    def test13(self):
        self.test_data = """L50
R300"""

        result = get_hit(self.test_data)

        self.assertEqual(4, result)

    def test14(self):
        self.test_data = """R50
R300"""

        result = get_hit(self.test_data)

        self.assertEqual(4, result)

if __name__ == "__main__":
    unittest.main()
