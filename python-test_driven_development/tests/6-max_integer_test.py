#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unit tests for the max_integer function"""

    def test_ordered_list(self):
        """Test with an ordered list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test with the maximum value at the beginning"""
        self.assertEqual(max_integer([10, 5, 8, 2]), 10)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        """Test with a list containing only one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_all_negative_numbers(self):
        """Test with a list of all negative numbers"""
        self.assertEqual(max_integer([-1, -5, -10, -2]), -1)

    def test_mixed_numbers(self):
        """Test with a mix of positive and negative numbers"""
        self.assertEqual(max_integer([-1, 5, 0, 10, -20]), 10)

    def test_floats(self):
        """Test with a list of floats"""
        self.assertEqual(max_integer([1.5, 2.7, 0.5]), 2.7)

if __name__ == '__main__':
    unittest.main()
