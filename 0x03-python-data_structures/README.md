# 0x03. Python - Data Structures: Lists, Tuples 
<img src="https://github.com/AyomideKayode/alx-higher_level_programming/blob/main/0x03-python-data_structures/main/Lists%20vs%20tuples.png?raw=true" alt="Lists vs Tuples" style="width: 100%;">

> Each file in this repository holds code that illustrates an essential concept of programming,
> specific to the Python programming language:
> Lists, Tuples & Data Structures.

## Resource

- [3.1.3. Lists](https://docs.python.org/3.4/tutorial/introduction.html#lists)
- [5. Data Structures](https://docs.python.org/3.4/tutorial/datastructures.html) (*until `5.3. Tuples and Sequences included`*)
- [Learn to Program 6 : Lists](https://www.youtube.com/watch?v=A1HUzrvS-Pw)

### General

* Why Python programming is awesome
* What are lists and how to use them
* What are the differences and similarities between strings and lists
* What are the most common methods of lists and how to use them
* How to use lists as stacks and queues
* What are list comprehensions and how to use them
* What are tuples and how to use them
* When to use tuples versus lists
* What is a sequence
* What is tuple packing
* What is sequence unpacking
* What is the <code>del</code> statement and how to use it
---
### Description of what each file shows (Tasks):

* main --- folder holds test files that showcase examples of how to use functions.
* lists.h --- holds the `.c` files' function prototypes.

* Files that start with:
0. [Print a list of integers](./0-print_list_integer.py) : A function that prints all integers of a list.
	- Prototype: `def print_list_integer(my_list=[]):`
	- Format: one integer per line.
	- You are not allowed to import any module
	- You can assume that the list only contains integers
	- You are not allowed to cast integers into strings
	- You have to use `str.format()` to print integers
	```sh
	guillaume@ubuntu:~/0x03$ ./0-main.py
	1
	2
	3
	4
	5
	guillaume@ubuntu:~/0x03$ 
	```
1. [Secure access to an element in a list](./1-element_at.py) : A function that retrieves an element from a list like in C.
	- Prototype: `def element_at(my_list, idx):`
	- If `idx` is negative, the function should return `None`
	- If `idx` is out of range (> of number of element in `my_list`), the function should return `None`
	- You are not allowed to import any module
	- You are not allowed to use `try/except`
	```sh
	guillaume@ubuntu:~/0x03$ ./1-main.py
	Element at index 3 is 4
	guillaume@ubuntu:~/0x03$ 
	```
2. [Replace element](./2-replace_in_list.py) : A function that replaces an element of a list at a specific position (like in C).
	- Prototype: `def replace_in_list(my_list, idx, element):`
	- If `idx` is negative, the function should not modify anything, and returns the original list
	- If `idx` is out of range (> of number of element in `my_list`), the function should not modify anything, and returns the original list
	- You are not allowed to import any module
	- You are not allowed to use `try/except`
	```sh
	guillaume@ubuntu:~/0x03$ ./2-main.py
	[1, 2, 3, 9, 5]
	[1, 2, 3, 9, 5]
	guillaume@ubuntu:~/0x03$ 
	```
3. [Print a list of integers... in reverse!](./3-print_reversed_list_integer.py) : A function that prints all integers of a list, in reverse order.
	- Prototype: `def print_reversed_list_integer(my_list=[]):`
	- Format: one integer per line.
	- You are not allowed to import any module
	- You can assume that the list only contains integers
	- You are not allowed to cast integers into strings
	- You have to use `str.format()` to print integers
	```sh
	guillaume@ubuntu:~/0x03$ ./3-main.py
	5
	4
	3
	2
	1
	guillaume@ubuntu:~/0x03$ 
	```
4. [Replace in a copy](4-new_in_list.py) : A function that replaces an element in a list at a specific position without modifying the original list (like in C).
	- Prototype: `def new_in_list(my_list, idx, element):`
	- If `idx` is negative, the function should return a copy of the original `list`
	- If `idx` is out of range (> of number of element in `my_list`), the function should return a copy of the original `list`
	- You are not allowed to import any module
	- You are not allowed to use `try/except`
	```sh
	guillaume@ubuntu:~/0x03$ ./4-main.py
	[1, 2, 3, 9, 5]
	[1, 2, 3, 4, 5]
	guillaume@ubuntu:~/0x03$ 
	```
5. [Can you C me now?](5-no_c.py) : A function that removes all characters `c` and `C` from a string.
	- Prototype: `def no_c(my_string):`
	- The function should return the new string
	- You are not allowed to import any module
	- You are not allowed to use `str.replace()`
	```sh
	guillaume@ubuntu:~/0x03$ ./5-main.py
	Best Shool
	hiago
	 is fun!
	guillaume@ubuntu:~/0x03$ 
	```
6. [Lists of lists = Matrix](6-print_matrix_integer.py) : A function that prints a matrix of integers.
	- Prototype: `def print_matrix_integer(matrix=[[]]):`
	- Format: see example
	- You are not allowed to import any module
	- You can assume that the list only contains integers
	- You are not allowed to cast integers into strings
	- You have to use `str.format()` to print integers
	```sh
	guillaume@ubuntu:~/0x03$ ./6-main.py | cat -e
	1 2 3$
	4 5 6$
	7 8 9$
	--$
	$
	guillaume@ubuntu:~/0x03$ 
	```
7. [Tuples addition](./7-add_tuple.py) : Write a function that adds 2 tuples.
	- Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
	- Returns a tuple with 2 integers:
		- The first element should be the addition of the first element of each argument
		- The second element should be the addition of the second element of each argument
	- You are not allowed to import any module
	- You can assume that the two tuples will only contain integers
	- If a tuple is smaller than 2, use the value `0` for each missing integer
	- If a tuple is bigger than 2, use only the first 2 integers
	```sh
	guillaume@ubuntu:~/0x03$ ./7-main.py
	(89, 100)
	(2, 89)
	(1, 89)
	guillaume@ubuntu:~/0x03$ 
	```
8. [More returns!](./8-multiple_returns.py) : Write a function that returns a tuple with the length of a string and its first character.
	- Prototype: `def multiple_returns(sentence):`
	- If the sentence is empty, the first character should be equal to `None`
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x03$ ./8-main.py
	Length: 22 - First character: A
	guillaume@ubuntu:~/0x03$ 
	```
9. [Find the max](./9-max_integer.py) : Write a function that finds the biggest integer of a list.
	- Prototype: `def max_integer(my_list=[]):`
	- If the list is empty, return `None`
	- You can assume that the list only contains integers
	- You are not allowed to import any module
	- You are not allowed to use the builtin `max()`
	```sh
	guillaume@ubuntu:~/0x03$ ./9-main.py
	Max: 90
	guillaume@ubuntu:~/0x03$ 
	```
10. [Only by 2](./10-divisible_by_2.py) : Write a function that finds all multiples of 2 in a list.
	- Prototype: `def divisible_by_2(my_list=[]):`
	- Return a new list with `True` or `False`, depending on whether the integer at the same position in the original list is a multiple of 2
	- The new list should have the same size as the original list
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x03$ ./10-main.py
	0 is divisible by 2
	1 is not divisible by 2
	2 is divisible by 2
	3 is not divisible by 2
	4 is divisible by 2
	5 is not divisible by 2
	6 is divisible by 2
	guillaume@ubuntu:~/0x03$ 
	```
11. [Delete at](./11-delete_at.py) : Write a function that deletes the item at a specific position in a list.
	- Prototype: `def delete_at(my_list=[], idx=0):`
	- If `idx` is negative or out of range, nothing change (returns the same list)
	- You are not allowed to use `pop()`
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x03$ ./11-main.py
	[1, 2, 3, 5]
	[1, 2, 3, 5]
	guillaume@ubuntu:~/0x03$ 
	```
12. [Switch](./12-switch.py) : Complete the source code in order to switch value of a and b
	- You can find the source code [here](https://github.com/alx-tools/0x03.py/blob/master/12-switch_py)
	- Your code should be inserted where the comment is (line 4)
	- Your program should be exactly 5 lines long
	```sh
	guillaume@ubuntu:~/py/0x03$ ./12-switch.py
	a=10 - b=89
	guillaume@ubuntu:~/py/0x03$ wc -l 12-switch.py
	5 12-switch.py
	guillaume@ubuntu:~/py/0x03$ 
	```
13. [Linked list palindrome](./13-is_palindrome.c), [lists.h](./lists.h) : 
	- Technical interview preparation:
	- You are not allowed to google anything
	- Whiteboard first
	- Write a function in C that checks if a singly linked list is a palindrome.
	- Prototype: int is_palindrome(listint_t **head);
	- Return: 0 if it is not a palindrome, 1 if it is a palindrome
	- An empty list is considered a palindrome
	```sh
	carrie@ubuntu:0x03$ gcc -Wall -Werror -Wextra -pedantic 13-main.c linked_lists.c 13-is_palindrome.c -o palindrome
	carrie@ubuntu:0x03$ ./palindrome
	1
	17
	972
	50
	98
	98
	50
	972
	17
	1
	Linked list is a palindrome
	carrie@ubuntu:0x03$
	```
14. [CPython #0: Python lists](./100-print_python_list_info.c) :
	- Create a C function that prints some basic info about Python lists.
	- Prototype: `void print_python_list_info(PyObject *p);`
	- Format: see example [show](100-test_lists.py)
	- Python version: 3.4 (and above)
	- Your shared library will be compiled with this command line: `gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c`
	- OS: Ubuntu 14.04 LTS
	- Start by reading:
		- listobject.h
		- object.h
		- [Common Object Structures](https://docs.python.org/3.4/c-api/structures.html)
		- [List Objects](https://docs.python.org/3.4/c-api/list.html)
	- For further understanding, this is my note on it: [C in Python](./main/Task%2014%20notes.md)

---
### Environment
* Language: Python 3.4.3 (and C for #13)
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
