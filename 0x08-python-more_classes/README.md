# Project: 0x08. Python - More Classes and Objects
<img src="./main/Judit-Polgar-Python-more-classes.jpg.crdownload" alt="Judit-Polgar" width=100%>

## Resources

#### Read or watch:

* [Object Oriented Programming](https://python.swaroopch.com/oop.html)
* [Object-Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php)
* [Class and Instance Attributes](https://python-course.eu/oop/class-instance-attributes.php)
* [classmethods and staticmethods](https://www.youtube.com/watch?v=rq8cL2XMM5M)
* [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
* [str vs repr](https://shipit.dev/posts/python-str-vs-repr.html)

## Learning Objectives

### General

* Why Python programming is awesome 
* What is OOP
* “first-class everything”
* What is a class
* What is an object and an instance
* What is the difference between a class and an object or instance
* What is an attribute
* What are and how to use public, protected and private attributes
* What is <code>self</code>
* What is a method
* What is the special <code>__init__</code> method and how to use it
* What is Data Abstraction, Data Encapsulation, and Information Hiding
* What is a property
* What is the difference between an attribute and a property in Python
* What is the Pythonic way to write getters and setters in Python
* What are the special <code>__str__</code> and <code>__repr__</code> methods and how to use them
* What is the difference between <code>__str__</code> and <code>__repr__</code>
* What is a class attribute
* What is the difference between a object attribute and a class attribute
* What is a class method
* What is a static method
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to object and classes
* What is and what does contain <code>__dict__</code> of a class and of an instance of a class
* How does Python find the attributes of an object or class
* How to use the <code>getattr</code> function

## Description of what each files shows (Tasks):
* **main**	--- main folder that holds all test case files on how to use function
* Files that start with:

0. [Simple rectangle](./0-rectangle.py) : Write an empty class `Rectangle` that defines a rectangle:
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x08$ ./0-main.py
	<class '0-rectangle.Rectangle'>
	{}
	guillaume@ubuntu:~/0x08$ 
	```
1. [Real definition of a rectangle](./1-rectangle.py) : Write a class `Rectangle` that defines a rectangle by: (based on `0-rectangle.py`)
	- Private instance attribute: `width:`
		- property `def width(self):` to retrieve it
		- property setter `def width(self, value):` to set it:
			- `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
			- if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
	- Private instance attribute: `height:`
		- property `def height(self):` to retrieve it
		- property setter `def height(self, value):` to set it:
			- `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
			- if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
	- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x08$ ./1-main.py
	{'_Rectangle__height': 4, '_Rectangle__width': 2}
	{'_Rectangle__height': 3, '_Rectangle__width': 10}
	guillaume@ubuntu:~/0x08$ 
	```
2. [Area and Perimeter](./2-rectangle.py) : Write a class `Rectangle` that defines a rectangle by: (based on `1-rectangle.py`)
	- Private instance attribute: `width:`
		- property `def width(self):` to retrieve it
		- property setter `def width(self, value):` to set it:
			- `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
			- if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
	- Private instance attribute: `height:`
		- property `def height(self):` to retrieve it
		- property setter `def height(self, value):` to set it:
			- `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
			- if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
	- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
	- Public instance method: `def area(self):` that returns the rectangle area
	- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
		- if `width` or `height` is equal to `0`, perimeter is equal to `0`
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x08$ ./2-main.py
	Area: 8 - Perimeter: 12
	--
	Area: 30 - Perimeter: 26
	guillaume@ubuntu:~/0x08$ 
	```
3. [String representation](./3-rectangle.py) : Write a class `Rectangle` that defines a rectangle by: (based on 2-rectangle.py)
	- Private instance attribute: `width:`
		- property `def width(self):` to retrieve it
		- property setter `def width(self, value):` to set it:
			- `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
			- if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
	- Private instance attribute: `height:`
		- property `def height(self):` to retrieve it
		- property setter `def height(self, value):` to set it:
			- `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
			- if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
	- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
	- Public instance method: `def area(self):` that returns the rectangle area
	- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
		- if `width` or `height` is equal to `0`, perimeter has to be equal to `0`
	- `print()` and `str()` should print the rectangle with the character `#`: see [3-main.py](./main/3-main.py)
		- if `width` or `height` is equal to `0`, return an empty string
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x08$ ./3-main.py
	Area: 8 - Perimeter: 12
	##
	##
	##
	##
	<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
	--
	##########
	##########
	##########
	<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
	guillaume@ubuntu:~/0x08$ 
	```
4. [Eval is magic](./4-rectangle.py) : Write a class `Rectangle` that defines a rectangle by: (based on `3-rectangle.py`)
	- Private instance attribute: `width:`
		- property `def width(self):` to retrieve it
		- property setter `def width(self, value):` to set it:
			- `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
			- if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
	- Private instance attribute: `height:`
		- property `def height(self):` to retrieve it
		- property setter `def height(self, value):` to set it:
			- `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
			- if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
	- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
	- Public instance method: `def area(self):` that returns the rectangle area
	- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
	- if `width` or `height` is equal to `0`, perimeter has to be equal to `0`
	- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
	- if `width` or `height` is equal to `0`, return an empty string
	- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` see [4-main.py](./main/4-main.py)
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x08$ ./4-main.py
	##
	##
	##
	##
	--
	##
	##
	##
	##
	--
	Rectangle(2, 4)
	--
	0x7f09ebf7cc88
	--
	##
	##
	##
	##
	--
	##
	##
	##
	##
	--
	Rectangle(2, 4)
	--
	0x7f09ebf7ccc0
	--
	False
	True
	guillaume@ubuntu:~/0x08$ 
	```
5. [Detect instance deletion](./5-rectangle.py) : Write a class `Rectangle` that defines a rectangle by: (based on `4-rectangle.py`)
	- Private instance attribute: `width:`
		- property `def width(self):` to retrieve it
		- property setter `def width(self, value):` to set it:
			- `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
			- if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
	- Private instance attribute: height:
		- property `def height(self):` to retrieve it
		- property setter `def height(self, value):` to set it:
			- `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
			- if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
	- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
	- Public instance method: `def area(self):` that returns the rectangle area
	- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
		- if `width` or `height` is equal to `0`, perimeter has to be equal to 0
	- `print()` and `str()` should print the rectangle with the character `#`:
		- if `width` or `height` is equal to 0, return an empty string
	- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
	- Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x08$ ./5-main.py
	Area: 8 - Perimeter: 12
	Bye rectangle...
	[NameError] name 'my_rectangle' is not defined
	guillaume@ubuntu:~/0x08$ 
	```
6. [How many instances](./6-rectangle.py) : Write a class `Rectangle` that defines a rectangle by: (based on `5-rectangle.py`)
	- Private instance attribute: `width:`
		- property `def width(self):` to retrieve it
		- property setter `def width(self, value):` to set it:
			- `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
			- if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
	- Private instance attribute: height:
		- property `def height(self):` to retrieve it
		- property setter `def height(self, value):` to set it:
			- `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
			- if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
	- Public class attribute `number_of_instances`:
		- Initialized to 0
		- Incremented during each new instance instantiation
		- Decremented during each instance deletion
	- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
	- Public instance method: `def area(self):` that returns the rectangle area
	- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
		- if `width` or `height` is equal to `0`, perimeter has to be equal to 0
	- `print()` and `str()` should print the rectangle with the character `#`:
		- if `width` or `height` is equal to 0, return an empty string
	- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
	- Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x08$ ./6-main.py
	2 instances of Rectangle
	Bye rectangle...
	1 instances of Rectangle
	Bye rectangle...
	0 instances of Rectangle
	guillaume@ubuntu:~/0x08$ 
	```
7. [Change representation](./7-rectangle.py) : Write a class `Rectangle` that defines a rectangle by: (based on `6-rectangle.py`)
	- Private instance attribute: `width:`
		- property `def width(self):` to retrieve it
		- property setter `def width(self, value):` to set it:
			- `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
			- if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
	- Private instance attribute: height:
		- property `def height(self):` to retrieve it
		- property setter `def height(self, value):` to set it:
			- `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
			- if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
	- Public class attribute `number_of_instances`:
		- Initialized to `0`
		- Incremented during each new instance instantiation
		- Decremented during each instance deletion
	- Public class attribute `print_symbol`:
		- Initialized to `#`
		- Used as symbol for string representation
		- Can be any type
	- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
	- Public instance method: `def area(self):` that returns the rectangle area
	- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
		- if `width` or `height` is equal to `0`, perimeter has to be equal to 0
	- `print()` and `str()` should print the rectangle with the character `#`:
		- if `width` or `height` is equal to 0, return an empty string
	- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
	- Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x08$ ./7-main.py
	########
	########
	########
	########
	--
	&&&&&&&&
	&&&&&&&&
	&&&&&&&&
	&&&&&&&&
	--
	##
	--
	CC
	--
	CCCCCCC
	CCCCCCC
	CCCCCCC
	--
	['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
	['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
	['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
	--
	Bye rectangle...
	Bye rectangle...
	Bye rectangle...
	guillaume@ubuntu:~/0x08$ 
	```
8. [Compare rectangles](./8-rectangle.py) : Write a class `Rectangle` that defines a rectangle by: (based on `6-rectangle.py`)
	- Private instance attribute: `width:`
		- property `def width(self):` to retrieve it
		- property setter `def width(self, value):` to set it:
			- `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
			- if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
	- Private instance attribute: height:
		- property `def height(self):` to retrieve it
		- property setter `def height(self, value):` to set it:
			- `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
			- if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
	- Public class attribute `number_of_instances`:
		- Initialized to `0`
		- Incremented during each new instance instantiation
		- Decremented during each instance deletion
	- Public class attribute `print_symbol`:
		- Initialized to `#`
		- Used as symbol for string representation
		- Can be any type
	- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
	- Public instance method: `def area(self):` that returns the rectangle area
	- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
		- if `width` or `height` is equal to `0`, perimeter has to be equal to 0
	- `print()` and `str()` should print the rectangle with the character `#`:
		- if `width` or `height` is equal to 0, return an empty string
	- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
	- Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
	- Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area
		- `rect_1` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_1 must be an instance of Rectangle`
		- `rect_2` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_2 must be an instance of Rectangle`
		- Returns `rect_1` if both have the same area value
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x08$ ./8-main.py
	my_rectangle_1 is bigger or equal to my_rectangle_2
	my_rectangle_2 is bigger than my_rectangle_1
	Bye rectangle...
	Bye rectangle...
	guillaume@ubuntu:~/0x08$ 
	```
9. [A square is a rectangle](./9-rectangle.py) : Write a class `Rectangle` that defines a rectangle by: (based on `6-rectangle.py`)
	- Private instance attribute: `width:`
		- property `def width(self):` to retrieve it
		- property setter `def width(self, value):` to set it:
			- `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
			- if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
	- Private instance attribute: height:
		- property `def height(self):` to retrieve it
		- property setter `def height(self, value):` to set it:
			- `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
			- if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
	- Public class attribute `number_of_instances`:
		- Initialized to `0`
		- Incremented during each new instance instantiation
		- Decremented during each instance deletion
	- Public class attribute `print_symbol`:
		- Initialized to `#`
		- Used as symbol for string representation
		- Can be any type
	- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
	- Public instance method: `def area(self):` that returns the rectangle area
	- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
		- if `width` or `height` is equal to `0`, perimeter has to be equal to 0
	- `print()` and `str()` should print the rectangle with the character `#`:
		- if `width` or `height` is equal to 0, return an empty string
	- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
	- Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
	- Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area
		- `rect_1` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_1 must be an instance of Rectangle`
		- `rect_2` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_2 must be an instance of Rectangle`
		- Returns `rect_1` if both have the same area value
	- Write a class `Rectangle` that defines a rectangle by: (based on `6-rectangle.py`)
	- Private instance attribute: `width:`
		- property `def width(self):` to retrieve it
		- property setter `def width(self, value):` to set it:
			- `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
			- if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
	- Private instance attribute: height:
		- property `def height(self):` to retrieve it
		- property setter `def height(self, value):` to set it:
			- `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
			- if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
	- Public class attribute `number_of_instances`:
		- Initialized to `0`
		- Incremented during each new instance instantiation
		- Decremented during each instance deletion
	- Public class attribute `print_symbol`:
		- Initialized to `#`
		- Used as symbol for string representation
		- Can be any type
	- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
	- Public instance method: `def area(self):` that returns the rectangle area
	- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
		- if `width` or `height` is equal to `0`, perimeter has to be equal to 0
	- `print()` and `str()` should print the rectangle with the character `#`:
		- if `width` or `height` is equal to 0, return an empty string
	- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
	- Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
	- Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area
		- `rect_1` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_1 must be an instance of Rectangle`
		- `rect_2` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_2 must be an instance of Rectangle`
		- Returns `rect_1` if both have the same area value
	- Class method `def square(cls, size=0):` that returns a new Rectangle instance with `width == height == size`
	- You are not allowed to import any module
	```guillaume@ubuntu:~/0x08$ ./9-main.py
	Area: 25 - Perimeter: 20
	#####
	#####
	#####
	#####
	#####
	Bye rectangle...
	guillaume@ubuntu:~/0x08$ 
	```
10. [N queens](./101-nqueens.py) : The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.
	- Usage: `nqueens N`
		- If the user called the program with the wrong number of arguments, print `Usage: nqueens N`, followed by a new line, and exit with the status `1`
	- where N must be an integer greater or equal to `4`
		- If N is not an integer, print `N must be a number`, followed by a new line, and exit with the status `1`
		- If N is smaller than `4`, print `N must be at least 4`, followed by a new line, and exit with the status `1`
	- The program should print every possible solution to the problem
		- One solution per line
		- Format: see example
		- You don’t have to print the solutions in a specific order
	- You are only allowed to import the `sys` module
	```sh
	julien@ubuntu:~/0x08. N Queens$ ./101-nqueens.py 4
	[[0, 1], [1, 3], [2, 0], [3, 2]]
	[[0, 2], [1, 0], [2, 3], [3, 1]]
	julien@ubuntu:~/0x08. N Queens$ ./101-nqueens.py 6
	[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
	[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
	[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
	[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
	julien@ubuntu:~/0x08. N Queens$ 
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

