# Project: 0x07. Python - Test-driven development

<img src="./main/Python-test-driven-development.gif" alt="Python-TDD" width=100%>

## Resources

#### Read or watch:

* [doctest — Test interactive Python examples](https://docs.python.org/3.4/library/doctest.html)<em>(until “26.2.3.7. Warnings” included)</em>
* [doctest – Testing through documentation](https://pymotw.com/3/doctest/)
* [Unit Tests in Python](https://www.youtube.com/watch?v=1Lfv5tUGsn8)
* [Unittest module](https://www.youtube.com/watch?v=6tNS--WetLI)
* [Interactive and Non-interactive tests](https://mattermost.com/blog/testing-python-understanding-doctest-and-unittest/)


### General

* Why Python programming is awesome
* What’s an interactive test
* Why tests are important
* How to write Docstrings to create tests
* How to write documentation for each module and function
* What are the basic option flags to create tests
* How to find edge cases


## Description of what each file shows (Tasks):

* **main** --- folder holds test files that showcase examples of how to use functions.

* **tests** --- folder that contains Python Test Cases files for the project. Using the doctest method of testing python functions.

* Files that start with:
0. [Integers addition](./0-add_integer.py), [Doctest-0](./tests/0-add_integer.txt) : Write a function that adds 2 integers.
	- Prototype: `def add_integer(a, b=98):`
	- `a` and `b` must be integers or floats, otherwise raise a `TypeError` exception with the message `a must be an integer` or `b must be an integer`
	- `a` and `b` must be first casted to integers if they are float
	- Returns an integer: the addition of `a` and `b`
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x07$ ./0-main.py
	3
	98
	100
	98
	b must be an integer
	a must be an integer
	guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
	9 passed and 0 failed.
	Test passed.
	guillaume@ubuntu:~/0x07$ python3 -c 'print(__import__("0-add_integer").__doc__)' | wc -l
	5
	guillaume@ubuntu:~/0x07$ python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)' | wc -l
	3
	guillaume@ubuntu:~/0x07$
	```
1. [Divide a matrix](./2-matrix_divided.py), [Doctest-2](./tests/2-matrix_divided.txt) : Write a function that divides all elements of a matrix.
	- Prototype: `def matrix_divided(matrix, div):`
	- `matrix` must be a list of lists of integers or floats, otherwise raise a `TypeError` exception with the message `matrix must be a matrix (list of lists) of integers/floats`
	- Each row of the `matrix` must be of the same size, otherwise raise a `TypeError` exception with the message `Each row of the matrix must have the same size`
	- `div` must be a number (integer or float), otherwise raise a `TypeError` exception with the message `div must be a number`
	- `div` can’t be equal to `0`, otherwise raise a `ZeroDivisionError` exception with the message `division by zero`
	- All elements of the `matrix` should be divided by `div`, rounded to 2 decimal places
	- Returns a new matrix
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x07$ ./2-main.py
	[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
	[[1, 2, 3], [4, 5, 6]]
	guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/2-matrix_divided.txt | tail -2
	5 passed and 0 failed.
	Test passed.
	guillaume@ubuntu:~/0x07$
	```
2. [Say my name](./3-say_my_name.py), [Doctest-3](./tests/3-say_my_name.txt) : Write a function that prints `My name is <first name> <last name>`

	- Prototype: `def say_my_name(first_name, last_name=""):`
	- `first_name` and `last_name` must be strings otherwise, raise a `TypeError` exception with the message `first_name must be a string` or `last_name must be a string`
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x07$ ./3-main.py | cat -e
	My name is John Smith$
	My name is Walter White$
	My name is Bob $
	first_name must be a string$
	guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/3-say_my_name.txt | tail -2
	5 passed and 0 failed.
	Test passed.
	guillaume@ubuntu:~/0x07$
	```
- **Note:** you might have a different number of tests than in the above example. As usual, your tests should cover all possible cases.
3. [Print square](./4-print_square.py), [Doctest-4](./tests/4-print_square.txt) : Write a function that prints a square with the character #.
	- Prototype: `def print_square(size):`
	- `size` is the size length of the square
	- `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
	- if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
	- if `size` is a float and is less than 0, raise a `TypeError` exception with the message `size must be an integer`
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x07$ ./4-main.py
	####
	####
	####
	####

	##########
	##########
	##########
	##########
	##########
	##########
	##########
	##########
	##########
	##########


	#

	size must be >= 0

	guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/4-print_square.txt
	guillaume@ubuntu:~/0x07$
	```
4. [Text indentation](./5-text_indentation.py), [Doctest-5](./tests/5-text_indentation.txt) : Write a function that prints a text with 2 new lines after each of these characters: `.`, `?` and `:`

	- Prototype: `def text_indentation(text):`
	- `text` must be a string, otherwise raise a `TypeError` exception with the message `text must be a string`
	- There should be no space at the beginning or at the end of each printed line
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x07$ ./5-main.py | cat -e
	Lorem ipsum dolor sit amet, consectetur adipiscing elit.$
	$
	Quonam modo?$
	$
	Utrum igitur tibi litteram videor an totas paginas commovere?$
	$
	Non autem hoc:$
	$
	igitur ne illud quidem.$
	$
	Fortasse id optimum, sed ubi illud:$
	$
	Plus semper voluptatis?$
	$
	Teneo, inquit, finem illi videri nihil dolere.$
	$
	Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens.$
	$
	Si id dicis, vicimus.$
	$
	Inde sermone vario sex illa a Dipylo stadia confecimus.$
	$
	Sin aliud quid voles, postea.$
	$
	Quae animi affectio suum cuique tribuens atque hanc, quam dico.$
	$
	Utinam quidem dicerent alium alio beatiorem! Iam ruinas videresguillaume@ubuntu:~/0x07$
	guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/5-text_indentation.txt
	guillaume@ubuntu:~/0x07$
	```
5. [Max integer - Unittest](./tests/6-max_integer_test.py) : Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.

- In this task, you will write unittests for the function `def max_integer(list=[]):`.
	- Your test file should be inside a folder `tests`
	- You have to use the [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
	- Your test file should be python files (extension: `.py`)
	- Your test file should be executed by using this command: `python3 -m unittest tests.6-max_integer_test`
	- All tests you make must be passable by the function below:
		- 🤥i.e. functions inside the 6-max_interger.py file
		- and 6-main.py
	```sh
	guillaume@ubuntu:~/0x07$ ./6-main.py
	4
	4
	guillaume@ubuntu:~/0x07$
	guillaume@ubuntu:~/0x07$ python3 -m unittest tests.6-max_integer_test 2>&1 | tail -1
	OK
	guillaume@ubuntu:~/0x07$
	guillaume@ubuntu:~/0x07$ head -7 tests/6-max_integer_test.py
	#!/usr/bin/python3
	"""Unittest for max_integer([..])
	"""
	import unittest
	max_integer = __import__('6-max_integer').max_integer

	class TestMaxInteger(unittest.TestCase):
	guillaume@ubuntu:~/0x07$
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
