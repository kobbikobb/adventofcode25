import unittest
from day03B.solution import get_solution


class TestDay03A(unittest.TestCase):

    def test1(self):
        test_data = """987654321111111"""

        result = get_solution(test_data)

        self.assertEqual(987654321111, result)

    def test2(self):
        test_data = """811111111111119"""

        result = get_solution(test_data)

        self.assertEqual(811111111119, result)


    def test3(self):
        test_data = """234234234234278"""

        result = get_solution(test_data)

        self.assertEqual(434234234278, result)

    def test5(self):
        test_data = """987654321111111
811111111111119
234234234234278
818181911112111"""

        result = get_solution(test_data)

        self.assertEqual(3121910778619, result)

if __name__ == "__main__":
    unittest.main()
