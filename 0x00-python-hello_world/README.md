# Project: 0x00. Python - Hello, World

## Table of Contents

- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Tasks](#tasks)
- [Environment](#environment)
- [Author](#author)

## Resources

#### Read or watch:

* [The Python tutorial](https://intranet.alxswe.com/rltoken/JsFCs_NBzMAR7-XPAZ9BoA)
	- [Whetting Your Appetite](https://intranet.alxswe.com/rltoken/kifRlLG2iMX5AZiW8lrCMg)
	- [Using the Python Interpreter](https://intranet.alxswe.com/rltoken/RVpfAuagCo9SdfYeoHd6jg)
	- [An Informal Introduction to Python](https://intranet.alxswe.com/rltoken/bVps0ZPWq7qVZ7vc-eJGTw)
* [How To Use String Formatters in Python 3](https://intranet.alxswe.com/rltoken/Ju0J8BxkuPX5yKZctyKfsQ)
* [Learn to Program](https://intranet.alxswe.com/rltoken/szBsJ-Qyig_RrImN7RGlOg)
* [Pycodestyle -- Style Guide for Python Code](https://intranet.alxswe.com/rltoken/tgYt-0zVy1T4sDlE9ohxnA)
## Learning Objectives

### General

* Why Python programming is awesome
* Who created Python
* Who is Guido van Rossum
* Where does the name ‘Python’ come from
* What is the Zen of Python
* How to use the Python interpreter
* How to print text and variables using <code>print</code>
* How to use strings
* What are indexing and slicing in Python
* What is the official Python coding style and how to check your code with <code>pycodestyle</code>
---
### Tasks

* main --- folder holds test files that showcase examples of how to use functions.
* lists.h --- holds the `.c` files' function prototypes.

* Files that start with:
0. [Run Python file](0-run) : Write a Shell script that runs a Python script.
	- The Python file name will be saved in the environment variable `$PYFILE`

	```sh
	guillaume@ubuntu:~/py/0x00$ cat main.py 
	#!/usr/bin/python3
	print("Holberton School")

	guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
	```
 
1. [Run inline](1-run_inline) : Write a Shell script that runs Python code.
	- The Python code will be saved in the environment variable `$PYCODE`

	```sh
	guillaume@ubuntu:~/py/0x00$ export PYCODE='print("Holberton School: {}".format(88+10))'
	```
 

2. [Hello, print](2-print.py) : Write a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.
	- Use the function `print`


3. [Print integer](3-print_number.py) : Complete the source code in order to print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.
	- You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py)
	- The output of the script should be:
		- the number, followed by `Battery street`,
		- followed by a new line.
	- You are not allowed to cast the variable `number` into a string.
	- Your code must be 3 lines long
	- You have to use the f-strings [tips](https://realpython.com/python-f-strings/)
	> C is strongly typed… not in Python! The variable `number`  can be assigned to a string, a float, a bool etc… Forcing the type during a string format (`"...".format(...)`) is a way to control the type of a variable


4. [Print float](4-print_float.py) : Complete the source code in order to print the float stored in the variable `number` with a precision of 2 digits.
	- You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/4-print_float.py)
	- The output of the program should be:
		- `Float:`, followed by the float with only two digits.
		- Followed by a new line.
	- You are not allowed to cast the variable `number` into a string.
	- You have to use the f-strings [tips](https://realpython.com/python-f-strings/)


5. [Print string](5-print_string.py) : Complete the source code in order to print 3 times a string stored in the variable `str`, followed by its first 9 characters.
	- You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py)
	- The output of the program should be:
		- 3 times the value of `str`
		- followed by a new line
		- followed by the 9 first characters of `str`
		- followed by a new line
	- You are not allowed to use any loops or conditional statement
	- Your program should be maximum 5 lines long


6. [Play with strings](6-concat.py) : Complete this source code to print `Welcome to Holberton School!`
	- You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py)
	- You are not allowed to use any loops or conditional statements.
	- You have to use the variables	`str1` and `str2` in your new line of code.
	- Your program should be exactly 5 lines long


7. [Copy - Cut - Paste](7-edges.py) : Complete this source code.
	- You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py)
	- You are not allowed to use any loops or conditional statements
	- Your program should be exactly 8 lines long
	- `word_first_3` should contain the first 3 letters of the variable `word`
	- `word_last_2` should contain the last 2 letters of the variable `word`
	- `middle_word` should contain the value of the variable `word` without the first and last letters.


8. [Create a new sentence](8-concat_edges.py) : Complete this source code to print `object-oriented programming with Python`, followed by a new line.
	- You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py)
	- You are not allowed to use any loops or conditional statements
	- Your program should be exactly 5 lines long
	- You are not allowed to create new variables
	- You are not allowed to use string literals
	> Asides the solution provided in my file, another method would have been to split the string into words with an array
	> and then call it back by the index...


9. [Easter Egg](9-easter_egg.py) : Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.
	- Your script should be maximum 98 characters long (please check with `wc -m 9-easter_egg.py`)
	- 😉Google is your friend


10. [Linked list cycle](10-check_cycle.c) Technical interview preparation:
	- You are not allowed to google anything
	- Whiteboard first
	- This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution’s runtime fast enough, does your solution require extra memory usage / mallocs, etc.
	- Write a function in C that checks if a singly linked list has a cycle in it.
		- Prototype: `int check_cycle(listint_t *list);`
		- Return: `0` if there is no cycle, `1` if there is a cycle
	- Requirements:
		- Only these functions are allowed: `write`, `printf`, `putchar`, `puts`, `malloc`, `free`
	- Compile the code this way: `gcc -Wall -Werror -Wextra -pedantic 10-main.c 10-check_cycle.c 10-linked_lists.c -o cycle`
	- The aim of the task in a nutshell: "Solving a problem is already a big win! but finding the best and optimal way to solve it, it’s way better! Think about the most optimal / fastest way to do it."
---


### Environment
* Language: Python 3.4.3 (and C for #10)
	* OS: Ubuntu 14.04 LTS
	* Compiler: python3 (and gcc 4.8.4)
	* Style guidelines: 
		- [PEP 8 (version 1.7)](https://www.python.org/dev/peps/pep-0008/)
		- [Betty style](https://github.com/holbertonschool/Betty/wiki)

---
### Author

Feel free to reach out to me through any of the following channels:

[![Beacons.ai Profile](https://img.shields.io/badge/Beacons.ai-cobbysefah-9cf?style=for-the-badge&logo=beacons&color=blue)](https://beacons.ai/cobbysefahsolomon)


[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:solomonsefah13@gmail.com)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/hunterxcobby)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/cobby-sefah-solomon-~-c-s-s-6460bb279/)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/cobby_is_a_god)
[![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/233557452729)
