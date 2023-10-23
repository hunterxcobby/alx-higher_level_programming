# Project: 0x05. Python - Exceptions

<img src="./main/Exceptions.gif" alt="Python-Exceptions" width="100%">

## Resources

#### **Read or watch:**

* [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
* [Learn to Program 11 Static & Exception Handling](https://www.youtube.com/watch?v=7vbgD-3s-w4)

### General

* Why Python programming is awesome 
* What’s the difference between errors and exceptions
* What are exceptions and how to use them
* When do we need to use exceptions
* How to correctly handle an exception
* What’s the purpose of catching exceptions
* How to raise a builtin exception
* When do we need to implement a clean-up action after an exception

---
## Description of what each file shows (Tasks):

* **main** --- folder holds test files that showcase examples of how to use functions.

* Files that start with:
0. [Safe list printing](./0-safe_print_list.py) : Write a function that prints x elements of a list.
	- Prototype: `def safe_print_list(my_list=[], x=0):`
	- `my_list` can contain any type (integer, string, etc.)
	- All elements must be printed on the same line followed by a new line.
	- `x` represents the number of elements to print
	- `x` can be bigger than the length of `my_list`
	- Returns the real number of elements printed
	- You have to use `try: / except:`
	- You are not allowed to import any module
	- You are not allowed to use `len()`
	```sh
	guillaume@ubuntu:~/0x05$ ./0-main.py
	12
	nb_print: 2
	12345
	nb_print: 5
	12345
	nb_print: 5
	guillaume@ubuntu:~/0x05$ 
	```
1. [Safe printing of an integers list](./1-safe_print_integer.py) : Write a function that prints an integer with `"{:d}".format()`.
	- Prototype: `def safe_print_integer(value):`
	- `value` can be any type (integer, string, etc.)
	- The integer should be printed followed by a new line
	- Returns `True` if `value` has been correctly printed (it means the value is an integer)
	- Otherwise, returns `False`
	- You have to use `try: / except:`
	- You have to use `"{:d}".format()` to print as integer
	- You are not allowed to import any module
	- You are not allowed to use `type()`
	```sh
	guillaume@ubuntu:~/0x05$ ./1-main.py
	89
	-89
	School is not an integer
	guillaume@ubuntu:~/0x05$ 
	```
2. [Print and count integers](./2-safe_print_list_integers.py) : Write a function that prints the first `x` elements of a list and only integers.
	- Prototype: `def safe_print_list_integers(my_list=[], x=0):`
	- `my_list` can contain any type (integer, string, etc.)
	- All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
	- `x` represents the number of elements to access in `my_list`
	- `x` can be bigger than the length of `my_list` - if it’s the case, an exception is expected to occur
	- Returns the real number of integers printed
	- You have to use `try: / except:`
	- You have to use `"{:d}".format()` to print an integer
	- You are not allowed to import any module
	- You are not allowed to use len()
	```sh
	guillaume@ubuntu:~/0x05$ ./2-main.py
	12
	nb_print: 2
	12345
	nb_print: 5
	12345Traceback (most recent call last):
	File "./2-main.py", line 14, in <module>
		nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
	File "/0x05/2-safe_print_list_integers.py", line 7, in safe_print_list_integers
		print("{:d}".format(my_list[i]), end="")
	IndexError: list index out of range
	guillaume@ubuntu:~/0x05$ 
	```
3. [Integers division with debug](./3-safe_print_division.py) : Write a function that divides 2 integers and prints the result.
	- Prototype: `def safe_print_division(a, b):`
	- You can assume that `a` and `b` are integers
	- The result of the division should print on the `finally:` section preceded by `Inside result:`
	- Returns the value of the division, otherwise: `None`
	- You have to use `try: / except: / finally:`
	- You have to use `"{}".format()` to print the result
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x05$ ./3-main.py
	Inside result: 6.0
	12 / 2 = 6.0
	Inside result: None
	12 / 0 = None
	guillaume@ubuntu:~/0x05$ 
	```
4. [Divide a list](./4-list_division.py) : Write a function that divides element by element 2 lists.
	- Prototype: `def list_division(my_list_1, my_list_2, list_length):`
	- `my_list_1` and `my_list_2` can contain any type (integer, string, etc.)
	- `list_length` can be bigger than the length of both lists
	- Returns a new list (length = `list_length`) with all divisions
	- If 2 elements can’t be divided, the division result should be equal to `0`
	- If an element is not an integer or float:
		- print: `wrong type`
	- If the division can’t be done (`/0`):
		- print: `division by 0`
	- If `my_list_1` or `my_list_2` is too short
		- print: `out of range`
	- You have to use `try: / except: / finally:`
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x05$ ./4-main.py
	[5.0, 2.0, 1.0]
	--
	division by 0
	wrong type
	out of range
	[5.0, 0, 0, 2.0, 0]
	guillaume@ubuntu:~/0x05$ 
	```
5. [Raise exception](./5-raise_exception.py) : Write a function that raises a type exception.
	- Prototype: `def raise_exception():`
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x05$ ./5-main.py
	Exception raised
	guillaume@ubuntu:~/0x05$ 
	```
6. [Raise a message](./6-raise_exception_msg.py) : Write a function that raises a name exception with a message.
	- Prototype: `def raise_exception_msg(message=""):`
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x05$ ./6-main.py
	C is fun
	guillaume@ubuntu:~/0x05$ 
	```
7. [Safe integer print with error message](./100-safe_print_integer_err.py) : Write a function that prints an integer.
	- Prototype: `def safe_print_integer_err(value):`
	- `value` can be any type (integer, string, etc.)
	- The integer should be printed followed by a new line
	- Returns `True` if `value` has been correctly printed (it means the value is an integer)
	- Otherwise, returns `False` and prints in `stderr` the error precede by `Exception:`
	- You have to use `try: / except:`
	- You have to use `"{:d}".format()` to print as integer
	- You are not allowed to use `type()`
	```sh
	guillaume@ubuntu:~/0x05$ ./100-main.py
	89
	-89
	Exception: Unknown format code 'd' for object of type 'str'
	School is not an integer
	guillaume@ubuntu:~/0x05$ ./100-main.py 2> /dev/null
	89
	-89
	School is not an integer
	guillaume@ubuntu:~/0x05$ 
	```
8. [Safe function](./101-safe_function.py) : Write a function that executes a function safely.
	- Prototype: `def safe_function(fct, *args):`
	- You can assume `fct` will be always a pointer to a function
	- Returns the result of the function,
	- Otherwise, returns `None` if something happens during the function and prints in `stderr` the error precede by `Exception:`
	- You have to use `try: / except:`
	```sh
	guillaume@ubuntu:~/0x05$ ./101-main.py
	result of my_div: 5.0
	Exception: division by zero
	result of my_div: None
	1
	2
	3
	4
	Exception: list index out of range
	result of print_list: None
	guillaume@ubuntu:~/0x05$ ./101-main.py 2> /dev/null
	result of my_div: 5.0
	result of my_div: None
	1
	2
	3
	4
	result of print_list: None
	guillaume@ubuntu:~/0x05$ 
	```
9. [ByteCode -> Python #4](./102-magic_calculation.py) : Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:
	```sh
	3           0 LOAD_CONST               1 (0)
				3 STORE_FAST               2 (result)

	4           6 SETUP_LOOP              94 (to 103)
				9 LOAD_GLOBAL              0 (range)
				12 LOAD_CONST               2 (1)
				15 LOAD_CONST               3 (3)
				18 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
				21 GET_ITER
			>>   22 FOR_ITER                77 (to 102)
				25 STORE_FAST               3 (i)

	5          28 SETUP_EXCEPT            49 (to 80)

	6          31 LOAD_FAST                3 (i)
				34 LOAD_FAST                0 (a)
				37 COMPARE_OP               4 (>)
				40 POP_JUMP_IF_FALSE       58

	7          43 LOAD_GLOBAL              1 (Exception)
				46 LOAD_CONST               4 ('Too far')
				49 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
				52 RAISE_VARARGS            1
				55 JUMP_FORWARD            18 (to 76)

	9     >>   58 LOAD_FAST                2 (result)
				61 LOAD_FAST                0 (a)
				64 LOAD_FAST                1 (b)
				67 BINARY_POWER
				68 LOAD_FAST                3 (i)
				71 BINARY_TRUE_DIVIDE
				72 INPLACE_ADD
				73 STORE_FAST               2 (result)
			>>   76 POP_BLOCK
				77 JUMP_ABSOLUTE           22

	10     >>   80 POP_TOP
				81 POP_TOP
				82 POP_TOP

	11          83 LOAD_FAST                1 (b)
				86 LOAD_FAST                0 (a)
				89 BINARY_ADD
				90 STORE_FAST               2 (result)

	12          93 BREAK_LOOP
				94 POP_EXCEPT
				95 JUMP_ABSOLUTE           22
				98 END_FINALLY
				99 JUMP_ABSOLUTE           22
			>>  102 POP_BLOCK

	13     >>  103 LOAD_FAST                2 (result)
				106 RETURN_VALUE
	```

---
### Environment
* Language: Python 3.4.3 (and C for #10)
	* OS: Ubuntu 14.04 LTS
	* Compiler: python3 (and gcc 4.8.4)
	* Style guidelines: 
		- [PEP 8 (version 1.7)](https://www.python.org/dev/peps/pep-0008/)
		- [Betty style](https://github.com/holbertonschool/Betty/wiki)

---
## Author

Feel free to reach out to me through any of the following channels:

[![Beacons.ai Profile](https://img.shields.io/badge/Beacons.ai-cobbysefah-9cf?style=for-the-badge&logo=beacons&color=blue)](https://beacons.ai/cobbysefahsolomon)


[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:solomonsefah13@gmail.com)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/hunterxcobby)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/cobby-sefah-solomon-~-c-s-s-6460bb279/)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/cobby_is_a_god)
[![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/233557452729)

## My Github Stats
![GitHub Stats](https://github-readme-stats.vercel.app/api?username=hunterxcobby&show_icons=true&count_private=true&hide_title=true&hide=prs&theme=radical)
