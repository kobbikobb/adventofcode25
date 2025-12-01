import unittest
from solution import part1, part2


class TestDay(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.test_data = """"""

    def test_part1(self):
        """Test part 1 with example data."""
        result = part1(self.test_data)
        self.assertEqual(result, None)

    def test_part2(self):
        """Test part 2 with example data."""
        result = part2(self.test_data)
        self.assertEqual(result, None)


if __name__ == "__main__":
    unittest.main()
