# Project: 0x0A. Python - Inheritance
<img src="./main/Inheritance in python.jfif" alt="Python-inheritance" width=100%>

## Resources

#### Read or watch:

* [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
* [Multiple inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)
* [Inheritance in Python](https://www.geeksforgeeks.org/inheritance-in-python/)
* [Learn to Program 10 : Inheritance Magic Methods](https://www.youtube.com/watch?v=d8kCdLCi6Lk)
## Learning Objectives

### General

* Why Python programming is awesome 
* What is a superclass, baseclass or parentclass
* What is a subclass
* How to list all attributes and methods of a class or instance
* When can an instance have new attributes
* How to inherit class from another
* How to define a class with multiple base classes 
* What is the default class every class inherit from
* How to override a method or attribute inherited from the base class
* Which attributes or methods are available by heritage to subclasses
* What is the purpose of inheritance
* What are, when and how to use <code>isinstance</code>, <code>issubclass</code>, <code>type</code> and <code>super</code> built-in functions

## Description of what each file shows (Tasks):
* main	--- folder that contains all test .py files to check projects.
* test	--- folder that contains the .txt files used to test functions created.
* Files that start with:

0. [Lookup](./0-lookup.py) : Write a function that returns the list of available attributes and methods of an object:
	- Prototype: `def lookup(obj):`
	- Returns a `list` object
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x0A$ ./0-main.py
	['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
	['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'my_attr1', 'my_meth']
	['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
	guillaume@ubuntu:~/0x0A$ 
	```
1. [My list](./1-my_list.py), [tests/1-my_list.txt](./tests/1-my_list.txt) : Write a class `MyList` that inherits from `list`:
	- Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)
	- You can assume that all the elements of the list will be of type `int`
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x0A$ ./1-main.py
	[1, 4, 2, 3, 5]
	[1, 2, 3, 4, 5]
	[1, 4, 2, 3, 5]
	guillaume@ubuntu:~/0x0A$ 
	```
2. [Exact same object](./2-is_same_class.py) : Write a function that returns `True` if the object is exactly an instance of the specified class ; otherwise `False`.
	- Prototype: `def is_same_class(obj, a_class):`
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x0A$ ./2-main.py
	1 is an instance of the class int
	guillaume@ubuntu:~/0x0A$ 
	```
3. [Same class or inherit from](./3-is_kind_of_class.py) : Write a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise `False`.
	- Prototype: def is_kind_of_class(obj, a_class):
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x0A$ ./3-main.py
	1 comes from int
	1 comes from object
	guillaume@ubuntu:~/0x0A$ 
	```
4. [Only sub class of](./4-inherits_from.py) : Write a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise `False`.
	- Prototype: `def inherits_from(obj, a_class):`
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x0A$ ./4-main.py
	True inherited from class int
	True inherited from class object
	guillaume@ubuntu:~/0x0A$ 
	```
5. [Geometry module](./5-base_geometry.py) : Write an empty class `BaseGeometry`.
	- You are not allowed to import any module.
	```sh
	guillaume@ubuntu:~/0x0A$ ./5-main.py
	<5-base_geometry.BaseGeometry object at 0x7f2050c69208>
	['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
	['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
	guillaume@ubuntu:~/0x0A$ 
	```
6. [Improve Geometry](./6-base_geometry.py) : Write a class `BaseGeometry` (based on `5-base_geometry.py`).
	- Public instance method: `def area(self):` that raises an `Exception` with the message `area is not implemented`
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x0A$ ./6-main.py
	[Exception] area() is not implemented
	guillaume@ubuntu:~/0x0A$ 
	```
7. [Integer validator](./7-base_geometry.py), [tests/7-base_geometry.txt](./tests/7-base_geometry.txt) : Write a class `BaseGeometry` (based on `6-base_geometry.py`).
	- Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
	- Public instance method: `def integer_validator(self, name, value):` that validates `value`:
		- you can assume `name` is always a string
		- if `value` is not an integer: raise a `TypeError` exception, with the message `<name> must be an integer`
		- if `value` is less or equal to 0: raise a `ValueError` exception with the message `<name> must be greater than 0`
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x0A$ ./7-main.py
	[TypeError] name must be an integer
	[ValueError] age must be greater than 0
	[ValueError] distance must be greater than 0
	guillaume@ubuntu:~/0x0A$ 
	```
8. [Rectangle](./8-rectangle.py) : Write a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`).
	- Instantiation with `width` and `height`: `def __init__(self, width, height):`
		- `width` and `height` must be private. No getter or setter
		- `width` and `height` must be positive integers, validated by `integer_validator`
	```sh
	guillaume@ubuntu:~/0x0A$ ./8-main.py
	<8-rectangle.Rectangle object at 0x7f6f488f7eb8>
	['_Rectangle__height', '_Rectangle__width', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'integer_validator']
	[AttributeError] 'Rectangle' object has no attribute 'width'
	[TypeError] height must be an integer
	guillaume@ubuntu:~/0x0A$ 
	```
9. [Full rectangle](./9-rectangle.py) : Write a class `Rectangle` that inherits from `BaseGeometry `(`7-base_geometry.py`). (task based on `8-rectangle.py`)
	- Instantiation with `width` and `height`: `def __init__(self, width, height):`:
		- `width` and `height` must be private. No getter or setter
		- `width` and `height` must be positive integers validated by `integer_validator`
	- the `area()` method must be implemented
	- `print()` should print, and `str()` should return, the following rectangle description: `[Rectangle] <width>/<height>`
	```sh
	guillaume@ubuntu:~/0x0A$ ./9-main.py
	[Rectangle] 3/5
	15
	guillaume@ubuntu:~/0x0A$ 
	```
10. [Square #1](./10-square.py) : Write a class `Square` that inherits from `Rectangle` (`9-rectangle.py`):
	- Instantiation with `size: def __init__(self, size):`:
		- `size` must be private. No getter or setter
		- `size` must be a positive integer, validated by `integer_validator`
	- the `area()` method must be implemented
	```sh
	guillaume@ubuntu:~/0x0A$ ./10-main.py
	[Rectangle] 13/13
	169
	guillaume@ubuntu:~/0x0A$ 
	```
11. Square #2 | [11-square.py](./11-square.py) : Write a class `Square` that inherits from `Rectangle` (`9-rectangle.py`). (task based on `10-square.py`).
	- Instantiation with size: `def __init__(self, size):`:
		- `size` must be private. No getter or setter
		- `size` must be a positive integer, validated by `integer_validator`
	- the `area()` method must be implemented
	- `print()` should print, and `str()` should return, the square description: `[Square] <width>/<height>`
	```sh
	guillaume@ubuntu:~/0x0A$ ./11-main.py
	[Square] 13/13
	169
	guillaume@ubuntu:~/0x0A$ 
	```
12. [My integer](./100-my_int.py) : Write a class `MyInt` that inherits from `int`:
	- `MyInt` is a rebel. `MyInt` has `==` and `!=` operators inverted
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x0A$ ./100-main.py
	3
	False
	True
	guillaume@ubuntu:~/0x0A$ 
	```
13. [Can I?](./101-add_attribute.py) : Write a function that adds a new attribute to an object if it’s possible:
	- Raise a `TypeError` exception, with the message `can't add new attribute` if the object can’t have new attribute
	- You are not allowed to use `try/except`
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x0A$ ./101-main.py
	John
	[TypeError] can't add new attribute
	guillaume@ubuntu:~/0x0A$ 
	```
---
### Environment
* Language: Python 3.4.3
    * OS: Ubuntu 14.04 LTS
    * Compiler: python3
    * Style guidelines:
        - [PEP 8 (version 1.7)](https://www.python.org/dev/peps/pep-0008/)

---
## Author

Feel free to reach out to me through any of the following channels:

[![Beacons.ai Profile](https://img.shields.io/badge/Beacons.ai-cobbysefah-9cf?style=for-the-badge&logo=beacons&color=blue)](https://beacons.ai/cobbysefahsolomon)


[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:solomonsefah13@gmail.com)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/hunterxcobby)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/cobby-sefah-solomon-~-c-s-s-6460bb279/)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/cobby_is_a_god)
[![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/233557452729)
