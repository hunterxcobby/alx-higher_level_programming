#!/usr/bin/python3

"""
Unittest for Base Class
# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_base.py
"""

import os
import unittest
import json
from models import base
from models import rectangle
from models import square
Base = base.Base
Rectangle = rectangle.Rectangle
Square = square.Square


class TestBase(unittest.TestCase):
    """TestBase Class"""

    def test_module_docstring(self):
        """
        Test if the module docstring is present.
        """
        self.assertTrue(len(__doc__) >= 1)

    def test_class_docstring(self):
        """
        Test if the Base class docstring is present.
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_id_assignment_with_id_argument(self):
        """Test to check whether the id attribute is assigned correctly
        when an id argument is provided during initialization.
        """
        base_instance = Base(42)
        self.assertEqual(base_instance.id, 42)
        my_base = Base(25)
        self.assertEqual(my_base.id, 25)

    def test_id_assignment_without_id_argument(self):
        """Test checks whether the id attribute is assigned correctly
        when no id argument is provided during initialization.
        And that it also increments.
        """
        base_instance = Base()
        base_instance2 = Base()
        # updated to 3 & 4 respectivly because of Task 18
        self.assertEqual(base_instance.id, 3)
        self.assertEqual(base_instance2.id, 4)

    def test_id_assignment_with_string(self):
        """Test to check if the id attribute would work correctly when
        a string type id is provided during initialization.
        """
        base_string = Base("Kazzywiz")
        self.assertEqual(base_string.id, "Kazzywiz")
        base_string2 = Base("Unittest")
        self.assertEqual(base_string2.id, "Unittest")

    def test_more_than_one_arg(self):
        """Test to confirm that Base class does indeed raises
        a TypeError if we pass in more than one args as id.
        """
        with self.assertRaises(TypeError):
            Base(42, 25)

    def test_type(self):
        self.assertEqual(type(Base), type)

    def test_id_reassignment(self):
        """Test to check if id can be reassigned a new value
        after initial initialization.
        """
        switch = Base(25)
        switch.id = 42
        self.assertEqual(42, switch.id)

    def test_to_json_string(self):
        list_of_dicts = [{'id': 1, 'name': 'Joy'}, {'id': 2, 'name': 'Bob'}]
        output = '[{"id": 1, "name": "Joy"}, {"id": 2, "name": "Bob"}]'
        result = Base.to_json_string(list_of_dicts)
        self.assertEqual(result, output)
        self.assertTrue(type(result) == str)

    def test_to_json_string_empty_list(self):
        list_of_dicts = []
        expected_output = '[]'
        json_str = Base.to_json_string(list_of_dicts)
        self.assertEqual(json_str, expected_output)

    def test_to_json_string_none(self):
        list_of_dicts = None
        expected_output = '[]'
        json_str = Base.to_json_string(list_of_dicts)
        self.assertEqual(json_str, expected_output)

    def test_save_to_file(self):
        """Test save to file with instance that inherited from Base.
        """
        r = Rectangle(10, 7, 2, 8, 99)
        r2 = Rectangle(2, 4, 2, 2, 98)
        Rectangle.save_to_file([r, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(
                json.dumps([r.to_dictionary(), r2.to_dictionary()]),
                file.read())

    def test_save_to_file_empty_list(self):
        """Test if empty list is given to be saved.
        """
        # Create an empty list
        list_of_objs = []
        # Save the empty list to a file
        filename = 'Rectangle.json'
        Rectangle.save_to_file(list_of_objs)
        # Read the saved file
        with open(filename, 'r') as my_file:
            saved_data = my_file.read()
        expected_data = '[]'  # Verify the saved data
        self.assertEqual(saved_data, expected_data)

    def test_save_to_file_none(self):
        # Save None to a file
        filename = 'Rectangle.json'
        Rectangle.save_to_file(None)
        # Read the saved file
        with open(filename, 'r') as my_file:
            saved_data = my_file.read()
        # Verify the saved data
        expected_data = '[]'
        self.assertEqual(saved_data, expected_data)

    def test_from_json_string(self):
        """Test that checks the method's basic functionality with a JSON string
        """
        json_string = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        json_output = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        result = Base.from_json_string(json_string)
        self.assertEqual(result, json_output)
        json_string = '[{"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}, \
        {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}]'
        json_output = Base.from_json_string(json_string)
        self.assertEqual(len(json_output), 2)
        self.assertTrue(type(json_output) is list)
        self.assertTrue(type(json_output[0]) is dict)
        self.assertTrue(type(json_output[1]) is dict)
        self.assertEqual(json_output[0],
                         {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8})
        self.assertEqual(json_output[1],
                         {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0})

    def test_from_json_string_empty_string(self):
        """Test that checks it with an empty string.
        """
        json_string = ''
        json_output = []
        result = Base.from_json_string(json_string)
        self.assertEqual(result, json_output)

    def test_from_json_string_none(self):
        """Test that checks it with a None argument.
        """
        json_string = None
        json_output = []
        result = Base.from_json_string(json_string)
        self.assertEqual(result, json_output)

    def test_create_rectangle(self):
        """Test to check the method's functionality for
        creating instances of Rectangle class.
        """
        dictionary = {'id': 42, 'width': 4, 'height': 3, 'x': 2, 'y': 1}
        r = Rectangle.create(**dictionary)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.id, 42)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 1)

    def test_create_square(self):
        """Test to check the method's functionality for
        creating instances of Square class.
        """
        dictionary = {'id': 42, 'size': 5, 'x': 2, 'y': 3}
        s = Square.create(**dictionary)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.id, 42)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_create_unsupported_class(self):
        """Test that checks if the method raises a ValueError
        when trying to create an instance of an unsupported class.
        """
        dictionary = {'id': 42, 'unsupported_attr': 'value'}
        with self.assertRaises(ValueError):
            Base.create(**dictionary)

    def test_load_from_file_rectangle(self):
        """Test load from file with the Rectangle instance.
        """
        # Create a JSON file with data for a Rectangle
        data = '[{"id": 42, "width": 4, "height": 3, "x": 2, "y": 1}]'
        filename = 'Rectangle.json'
        with open(filename, 'w') as file:
            file.write(data)

        # Load instances from the file
        instances = Rectangle.load_from_file()

        # Check the loaded instance
        self.assertIsInstance(instances, list)
        self.assertEqual(len(instances), 1)
        rect = instances[0]
        self.assertIsInstance(rect, Rectangle)
        self.assertEqual(rect.id, 42)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 1)

        # Clean up the created file
        os.remove(filename)

    def test_load_from_file_square(self):
        """Test load from file with the Rectangle instance.
        """
        # Create a JSON file with data for a Square
        data = '[{"id": 42, "size": 5, "x": 2, "y": 3}]'
        filename = 'Square.json'
        with open(filename, 'w') as file:
            file.write(data)

        # Load instances from the file
        instances = Square.load_from_file()

        # Check the loaded instance
        self.assertIsInstance(instances, list)
        self.assertEqual(len(instances), 1)
        s = instances[0]
        self.assertIsInstance(s, Square)
        self.assertEqual(s.id, 42)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

        # Clean up the created file, if you'd like
        # os.remove(filename)

    def test_load_from_file_none(self):
        """Test load from None file"""
        Rectangle.save_to_file(None)
        rect = Rectangle.load_from_file()
        self.assertEqual(type(rect), list)
        self.assertEqual(len(rect), 0)

    def test_load_from_file_empty(self):
        """Test load from empty file"""
        Rectangle.save_to_file([])
        rect = Rectangle.load_from_file()
        self.assertEqual(type(rect), list)
        self.assertEqual(len(rect), 0)

    def test_save_to_file_csv_rectangle(self):
        """Test to see that list of instances is serialized into CSV file.
        """
        # Create a list of Rectangle instances
        r1 = Rectangle(4, 3, 2, 1, 42)
        r2 = Rectangle(5, 4, 3, 2, 43)
        instances = [r1, r2]

        # Save the instances to a CSV file
        filename = 'Rectangle.csv'
        Base.save_to_file_csv(instances)

        # Read the saved file
        with open(filename, 'r', newline='') as my_file:
            lines = my_file.readlines()

        # Verify the saved data
        expected_data = ['42,4,3,2,1\n', '43,5,4,3,2\n']
        self.assertEqual(lines, expected_data)

        # Clean up the created file (optional)
        # os.remove(filename)

    def test_save_to_file_csv_square(self):
        """Test to see that list of instances is serialized into CSV file.
        """
        # Create a list of Square instances
        s1 = Square(5, 2, 3, 42)
        s2 = Square(6, 3, 4, 43)
        instances = [s1, s2]

        # Save the instances to a CSV file
        filename = 'Square.csv'
        Base.save_to_file_csv(instances)

        # Read the saved file
        with open(filename, 'r', newline='') as my_file:
            lines = my_file.readlines()

        # Verify the saved data
        expected_data = ['42,5,2,3\n', '43,6,3,4\n']
        self.assertEqual(lines, expected_data)

        # Clean up the created file (optional)
        # os.remove(filename)

    def test_save_to_file_csv_empty_list(self):
        # Create an empty list: nothing gets saved. Returns previous data.
        instances = []

        # Save the empty list to a CSV file
        filename = 'Square.csv'
        Base.save_to_file_csv(instances)

        # Read the saved file
        with open(filename, 'r', newline='') as my_file:
            lines = my_file.readlines()

        # Verify the saved data (should be data from the file before)
        # no new changes
        self.assertEqual(lines, ['42,5,2,3\n', '43,6,3,4\n'])

        # Clean up the created file (optional)
        # os.remove(filename)

    def test_load_from_file_csv_rectangle(self):
        """Test to see that list of instances is deserialized from a CSV file.
        """
        # Create a CSV file with data for Rectangle instances
        data = '42,4,3,2,1\n43,5,4,3,2\n'
        filename = 'Rectangle.csv'
        with open(filename, 'w', newline='') as my_file:
            my_file.write(data)

        # Load instances from the file
        instances = Rectangle.load_from_file_csv()

        # Check the loaded instances
        self.assertIsInstance(instances, list)
        self.assertEqual(len(instances), 2)
        r1 = instances[0]
        r2 = instances[1]
        self.assertIsInstance(r1, Rectangle)
        self.assertIsInstance(r2, Rectangle)
        self.assertEqual(r1.id, 42)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r2.id, 43)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 4)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 2)

        # Clean up the created file (optional)
        # os.remove(filename)

    def test_load_from_file_csv_square(self):
        # Create a CSV file with data for Square instances
        data = '42,5,2,3\n43,6,3,4\n'
        filename = 'Square.csv'
        with open(filename, 'w', newline='') as my_file:
            my_file.write(data)

        # Load instances from the file
        instances = Square.load_from_file_csv()

        # Check the loaded instances
        self.assertIsInstance(instances, list)
        self.assertEqual(len(instances), 2)
        s1 = instances[0]
        s2 = instances[1]
        self.assertIsInstance(s1, Square)
        self.assertIsInstance(s2, Square)
        self.assertEqual(s1.id, 42)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s2.id, 43)
        self.assertEqual(s2.size, 6)
        self.assertEqual(s2.x, 3)
        self.assertEqual(s2.y, 4)

        # Clean up the created file (optional)
        # os.remove(filename)


if __name__ == '__main__':
    unittest.main()
