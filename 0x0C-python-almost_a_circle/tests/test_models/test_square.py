#!/usr/bin/python3

"""
Unittest for Square Class
# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_square.py
"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_constructor(self):
        s = Square(5, 2, 3, 42)
        self.assertEqual(s.id, 42)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_constructor_defaults(self):
        s = Square(5)
        self.assertTrue(s.id is not None)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_args_count(self):
        """Test to check for exception when too many args are passed.
        """
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5, 6, 7)
        """Test to check for exception when too little args are passed.
        """
        with self.assertRaises(TypeError):
            Square()
            Square(None)

    def test_attribute_validation(self):
        """Test attributes are validated before set.
        And exceptions are being raised."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("10")
            Square([10, (3)])
            Square({20, '7'})
            Square({"d": 24})
            Square((6, 10), 8)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
            Square(9).size(-9)

    def test_str_print(self):
        """Test the __str__ method to verify that it prints out the string
        reprsentation of the Square attributes.
        """
        s = Square(5, 2, 3, 42)
        expected_output = "[Square] (42) 2/3 - 5"
        self.assertEqual(str(s), expected_output)

    def test_class(self):
        """Test that the Square instance class is initialized.
        """
        s = Square(24)
        self.assertEqual(type(s), Square)

    def test_size_property_invalid_type(self):
        """Test that errors are raised when invalid types are passed as size.
        """
        s = Square(12)
        with self.assertRaises(TypeError):
            s.size = "who-dey"

    def test_size_property_invalid_value(self):
        """Test that errors are raised when invalid values are passed as size.
        """
        s = Square(6)
        with self.assertRaises(ValueError):
            s.size = -2

    def test_update_with_args(self):
        """Test that the Square instance attributes are
        updated properly with args.
        """
        s = Square(5, 2, 3, 42)
        s.update(99, 7, 8, 9)
        self.assertEqual(s.id, 99)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 8)
        self.assertEqual(s.y, 9)

    def test_update_with_kwargs(self):
        """Test that the Square instance attributes are
        updated properly when args aren't provided.
        """
        s = Square(5, 2, 3, 42)
        s.update(size=7, x=8, y=9)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 8)
        self.assertEqual(s.y, 9)

    def test_size_property(self):
        """Test that the Square instance attributes are aligning with
        class attributes inherited from Parent class(Rectangle).
        """
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_to_dictionary(self):
        """Test that function returns the dictionary representation of the
        Square instance.
        """
        s = Square(5, 2, 3, 42)
        expected_output = {
            'id': 42,
            'size': 5,
            'x': 2,
            'y': 3
        }
        self.assertEqual(s.to_dictionary(), expected_output)
        s.update(99, 7, 8, 9)
        result = s.to_dictionary()
        expected_output = {
            'id': 99,
            'size': 7,
            'x': 8,
            'y': 9
        }
        self.assertEqual(result, expected_output)

    def test_to_dictionary_type(self):
        """Test that the Square instance initialized is actually a dict type.
        """
        s = Square(5, 2, 3, 42)
        result = s.to_dictionary()
        self.assertIsInstance(result, dict)


if __name__ == '__main__':
    unittest.main()
