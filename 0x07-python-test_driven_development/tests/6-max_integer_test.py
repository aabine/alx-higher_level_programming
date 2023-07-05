import unittest

max_integer = __import__("6-max_int").max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        self.assertEqual(max_integer([1]), 1)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 3, 2]), 3)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -3, -2]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 0, 5, -10]), 5)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([1, 2, 2]), 2)

if __name__ == '__main__':
    unittest.main()
