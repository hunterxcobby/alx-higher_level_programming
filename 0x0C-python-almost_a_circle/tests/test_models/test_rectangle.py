#!/usr/bin/python3

"""
Unittest for Rectangle Class
# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_rectangle.py
"""

import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys


class TestRectangle(unittest.TestCase):
    """TestRectangle Class"""

    # Attributes Test
    def test_rectangle_initialization(self):
        """Test to check that all attributes are correctly initialized.
        """
        r = Rectangle(4, 5, 2, 3, 1)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 1)

    def test_class(self):
        """Test that the Rectangle instance class is initialized.
        """
        rect = Rectangle(8, 11, 2, 3, 9)
        self.assertEqual(type(rect), Rectangle)

    def test_constructor_with_id_and_without(self):
        """Test to check that the Base id parameter is set upon
        initialization if provided and if not."""
        r = Rectangle(10, 20, 30, 40, 1)
        self.assertEqual(r.id, 1)
        r = Rectangle(10, 20, 30, 40)
        self.assertTrue(r.id is not None)

    def test_with_default_attr(self):
        """Test if default attributes are set when not given.
        """
        r2 = Rectangle(3, 4)
        self.assertTrue(r2.width == 3)
        self.assertTrue(r2.height == 4)
        self.assertTrue(r2.x == 0)
        self.assertTrue(r2.y == 0)
        self.assertTrue(r2.id is not None)

    def test_height_width_with_valid_value(self):
        """Test height and width reassignment with valid values.
        """
        r = Rectangle(6, 11)
        r.width = 15
        self.assertEqual(r.width, 15)
        r = Rectangle(4, 9)
        r.height = 7
        self.assertEqual(r.height, 7)

    def test_width_with_invalid_value(self):
        """Test height and width reassignment with invalid values.
        """
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.width = -5
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.height = -5

    def test_xy_with_valid_value(self):
        """Test x and y reassignment with valid values.
        """
        r = Rectangle(10, 20, 30, 40)
        r.x = 20
        self.assertEqual(r.x, 20)
        r = Rectangle(10, 20, 30, 40)
        r.y = 8
        self.assertEqual(r.y, 8)

    def test_xy_with_invalid_value(self):
        """Test x and y reassignment with invalid values.
        """
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.x = -5
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.y = -5

    def test_with_float_string_values(self):
        """Test attributes with float and string values.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect = Rectangle("invalid", 6)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect = Rectangle(8.27, 15)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect = Rectangle(3, "Fave")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect = Rectangle(4, 6.45)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect = Rectangle(3, 5, "square")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect = Rectangle(4, 9, 2.93)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect = Rectangle(7, 18, 4, "triangle")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect = Rectangle(8, 10, 4, 7.38)

    # Method Test
    def test_area(self):
        """Test that area function returns the area of
        Rectangle instance."""
        rect = Rectangle(9, 15)
        self.assertEqual(rect.area(), 135)
        rect = Rectangle(4, 8)
        self.assertEqual(rect.area(), 32)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_display_without_xy(self):
        """Test the display method with just width and height.
        """
        rect = Rectangle(3, 2)
        expected_output = "###\n###\n"
        captured_output = StringIO()
        sys.stdout = captured_output

        rect.display()
        sys.stdout = sys.__stdout__  # Restore stdout
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_display_with_xy(self):
        """Test the display method with all attributes.
        """
        rect = Rectangle(4, 3, 2, 1)
        expected_output = "\n  ####\n  ####\n  ####\n"
        captured_output = StringIO()
        sys.stdout = captured_output

        rect.display()
        sys.stdout = sys.__stdout__  # Restore stdout
        self.assertEqual(captured_output.getvalue(), expected_output)

        rect = Rectangle(5, 3, 3, 4)
        expected_output = "\n\n\n\n   #####\n   #####\n   #####\n"
        captured_output = StringIO()
        sys.stdout = captured_output

        rect.display()
        sys.stdout = sys.__stdout__  # Restore stdout
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_str_print(self):
        """Test the __str__ method to verify that it prints out the string
        reprsentation of the attributes.
        """
        rect = Rectangle(4, 3, 2, 1, 42)
        expected_output = "[Rectangle] (42) 2/1 - 4/3"
        self.assertEqual(str(rect), expected_output)

        rect = Rectangle(1, 2, 3, 4, 5)
        expected_output = '[Rectangle] (5) 3/4 - 1/2'
        self.assertEqual(str(rect), expected_output)

    def test_update_with_args(self):
        """Test method: update(*args)
        """
        rect = Rectangle(4, 3, 2, 1, 42)
        rect.update(99, 5, 6, 7, 8)
        self.assertEqual(rect.id, 99)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 6)
        self.assertEqual(rect.x, 7)
        self.assertEqual(rect.y, 8)

        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(63, 9, 10, 5, 6)
        self.assertEqual(str(rect), '[Rectangle] (63) 5/6 - 9/10')
        rect.update()
        self.assertEqual(str(rect), '[Rectangle] (63) 5/6 - 9/10')
        rect.update(74)
        self.assertEqual(str(rect), '[Rectangle] (74) 5/6 - 9/10')
        rect.update(85, 1)
        self.assertEqual(str(rect), '[Rectangle] (85) 5/6 - 1/10')
        rect.update(14, 1, 2)
        self.assertEqual(str(rect), '[Rectangle] (14) 5/6 - 1/2')
        rect.update(99, 1, 2, 3, 4)
        self.assertEqual(str(rect), '[Rectangle] (99) 3/4 - 1/2')
        """Test invalid *args"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect.update(87, 1, 2, 3, "Julien")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rect.update(45, 1, 2, 3, -6)

    def test_update_with_kwargs(self):
        """Test method: update(**kwargs)
        """
        rect = Rectangle(4, 3, 2, 1, 42)
        rect.update(id=79, width=5, height=6, x=7, y=8)
        self.assertEqual(str(rect), '[Rectangle] (79) 7/8 - 5/6')

        rect.update(nokey=1000, invalid=2000, testing=3000, id=4000)
        # Check that valid attributes are updated correctly
        self.assertEqual(rect.id, 4000)
        # Check that unexpected kwargs are ignored and do not affect attributes
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 6)
        self.assertEqual(rect.x, 7)
        self.assertEqual(rect.y, 8)
        with self.assertRaises(ValueError):
            rect.update(id=99, width=-5, height="Kante", x=3, y="Yktv")

    def test_to_dictionary_type(self):
        """Test that the result of function is actually a dictionary type.
        """
        rect = Rectangle(4, 3, 2, 1, 42)
        result = rect.to_dictionary()
        self.assertIsInstance(result, dict)

    def test_to_dictionary(self):
        """Test to verify that function returns dictionary representation
        of the Rectangle instance.
        """
        rect = Rectangle(4, 3, 2, 1, 42)
        rect.update(99, 7, 8, 9)
        result = rect.to_dictionary()
        expected_output = {
            'id': 99,
            'width': 7,
            'height': 8,
            'x': 9,
            'y': 1
        }
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
