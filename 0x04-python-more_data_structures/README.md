# Project: 0x04. Python - More Data Structures: Set, Dictionary
<img src="https://github.com/AyomideKayode/alx-higher_level_programming/blob/main/0x04-python-more_data_structures/main/python4.gif?raw=true">

> Each file in this repository holds code that illustrates an essential concept of programming,
> specific to the Python programming language: how to create and manipulate sets and dictionaries.

## Resources

#### Read or watch:

* [Data structures](https://docs.python.org/3/tutorial/datastructures.html)
* [Lambda, filter, reduce and map](https://python-course.eu/advanced-python/lambda-filter-reduce-map.php)
* [Learn to Program 12 Lambda Map Filter Reduce](https://www.youtube.com/watch?v=1GAC6KQUPeg)

### General

* Why Python programming is awesome
* What are sets and how to use them
* What are the most common methods of set and how to use them
* When to use sets versus lists
* How to iterate into a set
* What are dictionaries and how to use them
* When to use dictionaries versus lists or sets
* What is a key in a dictionary
* How to iterate over a dictionary
* What is a lambda function
* What are the map, reduce and filter functions
---
## Description of what each file shows (Tasks):

* main --- folder holds test files that showcase examples of how to use functions.

* Files that start with:
0. [Squared simple](./0-square_matrix_simple.py) : Write a function that computes the square value of all integers of a matrix.
	- Prototype: `def square_matrix_simple(matrix=[]):`
	- `matrix` is a 2 dimensional array
	- Returns a new matrix:
		- Same size as `matrix`
		- Each value should be the square of the value of the input
	- Initial matrix should not be modified
	- You are not allowed to import any module
	- You are allowed to use regular loops, `map`, etc.
	```sh
	guillaume@ubuntu:~/0x04$ ./0-main.py
	[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
	[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	guillaume@ubuntu:~/0x04$
	```
1. [Search and replace](./1-search_replace.py) : Write a function that replaces all occurrences of an element by another in a new list.
	- Prototype: `def search_replace(my_list, search, replace):`
	- `my_list` is the initial list
	- `search` is the element to replace in the list
	- `replace` is the new element
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x04$ ./1-main.py
	[1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
	[1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
	guillaume@ubuntu:~/0x04$ 
	```
2. [Unique addition](./2-uniq_add.py) : Write a function that adds all unique integers in a list (only once for each integer).
	- Prototype: `def uniq_add(my_list=[]):`
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x04$ ./2-main.py
	Result: 15
	guillaume@ubuntu:~/0x04$ 
	```
3. [Present in both](./3-common_elements.py) : Write a function that returns a set of common elements in two sets.
	- Prototype: `def common_elements(set_1, set_2):`
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x04$ ./3-main.py
	['C']
	guillaume@ubuntu:~/0x04$ 
	```
4. [Only differents](./4-only_diff_elements.py) : Write a function that returns a set of all elements present in only one set.
	- Prototype: `def only_diff_elements(set_1, set_2):`
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x04$ ./4-main.py
	['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']
	guillaume@ubuntu:~/0x04$ 
	```
5. [Number of keys](./5-number_keys.py) : Write a function that returns the number of keys in a dictionary.
	- Prototype: `def number_keys(a_dictionary):`
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x04$ ./5-main.py
	Number of keys: 3
	guillaume@ubuntu:~/0x04$ 
	```
6. [Print sorted dictionary](./6-print_sorted_dictionary.py) : Write a function that prints a dictionary by ordered keys.
	- Prototype: `def print_sorted_dictionary(a_dictionary):`
	- You can assume that all keys are strings
	- Keys should be sorted by alphabetic order
	- Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
	- Dictionary values can have any type
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x04$ ./6-main.py
	Number: 89
	ids: [1, 2, 3]
	language: C
	track: Low level
	guillaume@ubuntu:~/0x04$ 
	```
7. [Update dictionary](./7-update_dictionary.py) : Write a function that replaces or adds key/value in a dictionary.
	- Prototype: def update_dictionary(a_dictionary, key, value):
	- `key` argument will be always a string
	- `value` argument will be any type
	- If a key exists in the dictionary, the value will be replaced
	- If a key doesn’t exist in the dictionary, it will be created
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x04$ ./7-main.py
	language: Python
	number: 89
	track: Low level
	--
	language: Python
	number: 89
	track: Low level
	--
	--
	city: San Francisco
	language: Python
	number: 89
	track: Low level
	--
	city: San Francisco
	language: Python
	number: 89
	track: Low level
	guillaume@ubuntu:~/0x04$ 
	```
8. [Simple delete by key](./8-simple_delete.py) : Write a function that deletes a key in a dictionary.
	- Prototype: `def simple_delete(a_dictionary, key=""):`
	- `key` argument will be always a string
	- If a key doesn’t exist, the dictionary won’t change
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x04$ ./8-main.py
	Number: 89
	ids: [1, 2, 3]
	language: C
	--
	Number: 89
	ids: [1, 2, 3]
	language: C
	--
	--
	Number: 89
	ids: [1, 2, 3]
	language: C
	--
	Number: 89
	ids: [1, 2, 3]
	language: C
	guillaume@ubuntu:~/0x04$ 
	```
9. [Multiply by 2](./9-multiply_by_2.py) : Write a function that returns a new dictionary with all values multiplied by 2
	- Prototype: `def multiply_by_2(a_dictionary):`
	- You can assume that all values are only integers
	- Returns a new dictionary
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x04$ ./9-main.py
	Alex: 8
	Bob: 14
	John: 12
	Mike: 14
	Molly: 16
	--
	Alex: 16
	Bob: 28
	John: 24
	Mike: 28
	Molly: 32
	guillaume@ubuntu:~/0x04$ 
	```
10. [Best score](./10-best_score.py) : Write a function that returns a key with the biggest integer value.
	- Prototype: `def best_score(a_dictionary):`
	- You can assume that all values are only integers
	- If no score found, return `None`
	- You can assume all students have a different score
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x04$ ./10-main.py
	Best score: Molly
	Best score: None
	guillaume@ubuntu:~/0x04$ 
	```
11. [Multiply by using map](./11-multiply_list_map.py) : Write a function that returns a list with all values multiplied by a number without using any loops.
	- Prototype: `def multiply_list_map(my_list=[], number=0):`
	- Returns a new list:
		- Same length as `my_list`
		- Each value should be multiplied by `number`
	- Initial list should not be modified
	- You are not allowed to import any module
	- You have to use `map`
	- Your file should be max 3 lines
	```sh
	guillaume@ubuntu:~/0x04$ ./11-main.py
	[4, 8, 12, 16, 24]
	[1, 2, 3, 4, 6]
	guillaume@ubuntu:~/0x04$ 
	```
12. [Roman to Integer](./12-roman_to_int.py) : 
	- Technical interview preparation:
		- You are not allowed to google anything
		- Whiteboard first
	- Create a function `def roman_to_int(roman_string):` that converts a Roman numeral to an integer.
		- You can assume the number will be between 1 to 3999.
		- `def roman_to_int(roman_string)` must return an integer
		- If the `roman_string` is not a string or `None`, return 0
	```sh
	guillaume@ubuntu:~/0x04$ ./12-main.py
	X = 10
	VII = 7
	IX = 9
	LXXXVII = 87
	DCCVII = 707
	guillaume@ubuntu:~/0x04$ 
	```
13. [Weighted average!](./100-weight_average.py) : Write a function that returns the weighted average of all integers tuple `(<score>, <weight>)`
	- Prototype: `def weight_average(my_list=[]):`
	- Returns 0 if the list is empty
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x04$ ./100-main.py
	Average: 2.80
	guillaume@ubuntu:~/0x04$ 
	```
14. [Squared by using map](./101-square_matrix_map.py) : Write a function that computes the square value of all integers of a matrix using map
	- Prototype: `def square_matrix_map(matrix=[]):`
	- `matrix` is a 2 dimensional array
	- Returns a new matrix:
		- Same size as `matrix`
		- Each value should be the square of the value of the input
	- Initial matrix should not be modified
	- You are not allowed to import any module
	- You have to use `map`
	- You are not allowed to use `for` or `while`
	- Your file should be max 3 lines
	```sh
	guillaume@ubuntu:~/0x04$ ./101-main.py
	[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
	[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	guillaume@ubuntu:~/0x04$ 
	```
15. [Delete by value](./102-complex_delete.py) : Write a function that deletes keys with a specific value in a dictionary.
	- Prototype: `def complex_delete(a_dictionary, value):`
	- If the value doesn’t exist, the dictionary won’t change
	- All keys having the searched value have to be deleted
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x04$ ./102-main.py
	ids: [1, 2, 3]
	track: Low
	--
	ids: [1, 2, 3]
	track: Low
	--
	--
	ids: [1, 2, 3]
	track: Low
	--
	ids: [1, 2, 3]
	track: Low
	guillaume@ubuntu:~/0x04$ 
	```
16. [CPython #1: PyBytesObject](./103-python.c) : Create two C functions that print some basic info about Python lists and Python bytes objects.
* Python lists:
	- Prototype: `void print_python_list(PyObject *p);`
	- Format: see example
* Python bytes:
	- Prototype: `void print_python_bytes(PyObject *p);`
	- Format: see example
	- Line “first X bytes”: print a maximum of 10 bytes
	- If `p` is not a valid `PyBytesObject`, print an error message (see example)
	- Read `/usr/include/python3.4/bytesobject.h`
* About:
	- Python version: 3.4 `(and above, might need to update compiler path if higher version.)`
	- Your shared library will be compiled with this command line: `gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c`
	- You are not allowed to use the following macros/functions:
		- `Py_SIZE`
		- `Py_TYPE`
		- `PyList_GetItem`
		- `PyBytes_AS_STRING`
		- `PyBytes_GET_SIZE`
	```sh
	julien@ubuntu:~/CPython$ python3 --version
	Python 3.4.3
	julien@ubuntu:~/CPython$ gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c
	julien@ubuntu:~/CPython$ cat 103-tests.py 
	import ctypes

	lib = ctypes.CDLL('./libPython.so')
	lib.print_python_list.argtypes = [ctypes.py_object]
	lib.print_python_bytes.argtypes = [ctypes.py_object]
	s = b"Hello"
	lib.print_python_bytes(s);
	b = b'\xff\xf8\x00\x00\x00\x00\x00\x00';
	lib.print_python_bytes(b);
	b = b'What does the \'b\' character do in front of a string literal?';
	lib.print_python_bytes(b);
	l = [b'Hello', b'World']
	lib.print_python_list(l)
	del l[1]
	lib.print_python_list(l)
	l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], b"Holberton", "Betty"]
	lib.print_python_list(l)
	l = []
	lib.print_python_list(l)
	l.append(0)
	lib.print_python_list(l)
	l.append(1)
	l.append(2)
	l.append(3)
	l.append(4)
	lib.print_python_list(l)
	l.pop()
	lib.print_python_list(l)
	l = ["Holberton"]
	lib.print_python_list(l)
	lib.print_python_bytes(l);
	julien@ubuntu:~/CPython$ python3 103-tests.py 
	[.] bytes object info
	size: 5
	trying string: Hello
	first 6 bytes: 48 65 6c 6c 6f 00
	[.] bytes object info
	size: 8
	trying string: �
	first 9 bytes: ff f8 00 00 00 00 00 00 00
	[.] bytes object info
	size: 60
	trying string: What does the 'b' character do in front of a string literal?
	first 10 bytes: 57 68 61 74 20 64 6f 65 73 20
	[*] Python list info
	[*] Size of the Python List = 2
	[*] Allocated = 2
	Element 0: bytes
	[.] bytes object info
	size: 5
	trying string: Hello
	first 6 bytes: 48 65 6c 6c 6f 00
	Element 1: bytes
	[.] bytes object info
	size: 5
	trying string: World
	first 6 bytes: 57 6f 72 6c 64 00
	[*] Python list info
	[*] Size of the Python List = 1
	[*] Allocated = 2
	Element 0: bytes
	[.] bytes object info
	size: 5
	trying string: Hello
	first 6 bytes: 48 65 6c 6c 6f 00
	[*] Python list info
	[*] Size of the Python List = 8
	[*] Allocated = 8
	Element 0: bytes
	[.] bytes object info
	size: 5
	trying string: Hello
	first 6 bytes: 48 65 6c 6c 6f 00
	Element 1: int
	Element 2: int
	Element 3: float
	Element 4: tuple
	Element 5: list
	Element 6: bytes
	[.] bytes object info
	size: 9
	trying string: Holberton
	first 10 bytes: 48 6f 6c 62 65 72 74 6f 6e 00
	Element 7: str
	[*] Python list info
	[*] Size of the Python List = 0
	[*] Allocated = 0
	[*] Python list info
	[*] Size of the Python List = 1
	[*] Allocated = 4
	Element 0: int
	[*] Python list info
	[*] Size of the Python List = 5
	[*] Allocated = 8
	Element 0: int
	Element 1: int
	Element 2: int
	Element 3: int
	Element 4: int
	[*] Python list info
	[*] Size of the Python List = 4
	[*] Allocated = 8
	Element 0: int
	Element 1: int
	Element 2: int
	Element 3: int
	[*] Python list info
	[*] Size of the Python List = 1
	[*] Allocated = 1
	Element 0: str
	[.] bytes object info
	[ERROR] Invalid Bytes Object
	julien@ubuntu:~/CPython$ 
	```
---
### Environment
* Language: Python 3.4.3 (and C for #16)
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

## My Github Stats
![GitHub Stats](https://github-readme-stats.vercel.app/api?username=hunterxcobby&show_icons=true&count_private=true&hide_title=true&hide=prs&theme=radical)
