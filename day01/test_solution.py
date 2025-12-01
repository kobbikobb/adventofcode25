import unittest
from solution import part1, part2


class TestDay01(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.test_data = """10
20
30
Hello World
40
50"""

    def test_part1(self):
        """Test part 1: Count lines."""
        result = part1(self.test_data)
        self.assertEqual(result, 6)

    def test_part2(self):
        """Test part 2: Sum numbers."""
        result = part2(self.test_data)
        self.assertEqual(result, 150)

    def test_part1_single_line(self):
        """Test part 1 with single line."""
        result = part1("single")
        self.assertEqual(result, 1)

    def test_part2_no_numbers(self):
        """Test part 2 with no numbers."""
        result = part2("hello\nworld")
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
