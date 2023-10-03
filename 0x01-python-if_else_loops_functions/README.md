# Project: 0x01. Python - if/else, loops, functions
![img](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/233/code.png)
> Each file in this repository holds code that illustrates an essential concept of programming,
> specific to the Python programming language: `if/elif/else`, `loops`, `range`, `ord()`, `chr()`,
>  modulo, copy of string, bytecode

## Resources

#### Read or watch:

* [More Control Flow Tools](https://intranet.alxswe.com/rltoken/jpjs5EnZTpBLLEremJYjPQ)
* [IndentationError](https://intranet.alxswe.com/rltoken/F9n2AE-fpEPzt2PfBMGYAQ)
* [How To Use String Formatters in Python 3](https://intranet.alxswe.com/rltoken/ZdtRIAkFu8dMBT99DcFBNg)
* [Learn to Program](https://intranet.alxswe.com/rltoken/ElQgZYNHrLI7kV_ysEB1hQ)
* [Learn to Program 2 : Looping](https://intranet.alxswe.com/rltoken/ElQgZYNHrLI7kV_ysEB1hQ)
* [Pycodestyle -- Style Guide for Python Code](https://intranet.alxswe.com/rltoken/TuTTnEg_Rwn8U1g3PEsZmA)
## Learning Objectives

### General

* Why Python programming is awesome
* Why indentation is so important in Python
* How to use the <code>if</code>, <code>if ... else</code> statements
* How to use comments
* How to affect values to variables
* How to use the <code>while</code> and <code>for</code> loops
* How is Python’s <code>for</code> different from <code>C</code>‘s?
* How to use the <code>break</code> and <code>continues</code> statements
* How to use <code>else</code> clauses on loops
* What does the <code>pass</code> statement do, and when to use it
* How to use <code>range</code>
* What is a function and how do you use functions
* What does return a function that does not use any <code>return</code> statement
* Scope of variables
* What’s a traceback
* What are the arithmetic operators and how to use them
---
### Description of what each file shows (Tasks):

* main --- folder holds test files that showcase examples of how to use functions.
* lists.h --- holds the `.c` files' function prototypes.

* Files that start with:
0. [Positive anything is better than negative nothing](0-positive_or_negative.py) : This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print whether the number stored in the variable `number` is positive or negative.
	- You can find the source code [here](https://github.com/holbertonschool/0x01.py/blob/master/0-positive_or_negative_py)
	- The variable `number` will store a different value every time you will run this program.
	- You don’t have to understand what `import`, `random. randint` do. Please do not touch this code.
	- The output of the program should be:
		- The number, followed by
			- if the number is greater than 0: `is positive`
			- if the number is 0: `is zero`
			- if the number is less than 0; `is negative`
		- followed by a new line.
1. [The last digit](1-last_digit.py) : This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable `number`.
	- You can find the source code [here](https://github.com/holbertonschool/0x01.py/blob/master/1-last_digit_py)
	- The variable `number` will store a different value every time you will run this program.
	- You don’t have to understand what `import`, `random. randint` do. Please do not touch this code. This line should not change: `number = random.randint(-10000,10000)`
	- The output of the program should be:
		- The string `Last digit of`, followed by
		- the number, followed by
		- the string `is`, followed by the last digit of `number`, followed by
			- if the last digit is greater than 5: the string `and is greater than 5`
			- if the last digit is 0: the string `and is 0`
			- if the last digit is less than 6 and not 0: the string `and is less than 6 and not 0`
		- followed by a new line.
	```
	guillaume@ubuntu:~/0x01$ ./1-last_digit.py
	Last digit of -9200 is 0 and is 0
	guillaume@ubuntu:~/0x01$ ./1-last_digit.py
	Last digit of 5247 is 7 and is greater than 5
	guillaume@ubuntu:~/0x01$ ./1-last_digit.py
	Last digit of -9318 is -8 and is less than 6 and not 0
	guillaume@ubuntu:~/0x01$ ./1-last_digit.py
	Last digit of 3369 is 9 and is greater than 5
	guillaume@ubuntu:~/0x01$ ./1-last_digit.py
	Last digit of -5224 is -4 and is less than 6 and not 0
	guillaume@ubuntu:~/0x01$ ./1-last_digit.py
	Last digit of -4485 is -5 and is less than 6 and not 0
	guillaume@ubuntu:~/0x01$ ./1-last_digit.py
	Last digit of 3850 is 0 and is 0
	```	
2. [I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game](2-print_alphabet.py) : Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
	- You can only use one `print` function with string format
	- You can only use one loop in your code
	- You are not allowed to store characters in a variable
	- You are not allowed to import any module
	```
	guillaume@ubuntu:~/0x01$ ./2-print_alphabet.py
	abcdefghijklmnopqrstuvwxyzguillaume@ubuntu:~/0x01$
	```
3. [When I was having that alphabet soup, I never thought that it would pay off](3-print_alphabt.py) : Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
	- Print all the letters except `q` and `e`
	- You can only use one `print` function with string format
	- You can only use one loop in your code
	- You are not allowed to store characters in a variable
	- You are not allowed to import any module
	```
	guillaume@ubuntu:~/0x01$ ./3-print_alphabt.py
	abcdfghijklmnoprstuvwxyzguillaume@ubuntu:~/0x01$
	```
4. [Hexadecimal printing](4-print_hexa.py) : Write a program that prints all numbers from `0` to `98` in decimal and in hexadecimal (as in the following example)
	- Print all the letters except `q` and `e`
	- You can only use one `print` function with string format
	- You can only use one loop in your code
	- You are not allowed to store characters in a variable
	- You are not allowed to import any module
	```
	guillaume@ubuntu:~/0x01$ ./4-print_hexa.py
	0 = 0x0
	1 = 0x1
	2 = 0x2
	3 = 0x3
	4 = 0x4
	5 = 0x5
	6 = 0x6
	7 = 0x7
	8 = 0x8
	9 = 0x9
	10 = 0xa
	11 = 0xb
	12 = 0xc
	13 = 0xd
	14 = 0xe
	15 = 0xf
	16 = 0x10
	17 = 0x11
	18 = 0x12
	...
	96 = 0x60
	97 = 0x61
	98 = 0x62
	guillaume@ubuntu:~/0x01$
	```
5. [00...99](5-print_comb2.py) : Write a program that prints numbers from `0` to `99`.
	- Numbers must be separated by `,`, followed by a space
	- Numbers should be printed in ascending order, with two digits
	- The last number should be followed by a new line
	- You can only use no more than 2 `print` functions with string format
	- You can only use one loop in your code
	- You are not allowed to store numbers or strings in a variable
	- You are not allowed to import any module
	```
	guillaume@ubuntu:~/0x01$ ./5-print_comb2.py
	00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
	21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 
	41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 
	61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 
	81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99
	guillaume@ubuntu:~/0x01$ 
	```
6. [Inventing is a combination of brains and materials. The more brains you use, the less material you need](6-print_comb3.py) : Write a program that prints all possible different combinations of two digits.
	- Numbers must be separated by `,`, followed by a space
	- The two digits must be different
	- `01` and `10` are considered the same combination of the two digits `0` and `1`
	- Print only the smallest combination of two digits
	- Numbers should be printed in ascending order, with two digits
	- The last number should be followed by a new line
	- You can only use no more than 3 `print` functions with string format
	- You can only use no more than 2 loops in your code
	- You are not allowed to store numbers or strings in a variable
	- You are not allowed to import any module
	```
	guillaume@ubuntu:~/0x01$ ./6-print_comb3.py
	01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 
	28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89
	guillaume@ubuntu:~/0x01$ 
	```
7. [islower](7-islower.py) : Write a function that checks for lowercase character.
	- Prototype: `def islower(c):`
	- Returns `True` if `c` is lowercase
	- Returns `False` otherwise
	- You are not allowed to import any module
	- You are not allowed to use `str.upper()` and `str.isupper()`
	- **Tips:** [ord()](https://docs.python.org/3.4/library/functions.html?highlight=ord#ord)
	- You don’t need to understand `__import__`
	```
	guillaume@ubuntu:~/0x01$ ./7-main.py
	a is lower
	H is upper
	A is upper
	3 is upper
	g is lower
	guillaume@ubuntu:~/0x01$ 
	```
8. [To uppercase](8-uppercase.py) : Write a function that prints a string in uppercase followed by a new line.
	- Prototype: `def uppercase(str):`
	- You can only use no more than 2 `print` functions with string format
	- You can only use one loop in your code
	- You are not allowed to import any module
	- You are not allowed to use `str.upper()` and `str.isupper()`
	- **Tips:** [ord()](https://docs.python.org/3.4/library/functions.html?highlight=ord#ord)
	- You don’t need to understand `__import__`
	```
	guillaume@ubuntu:~/0x01$ ./8-main.py
	BEST
	BEST SCHOOL 98 BATTERY STREET
	guillaume@ubuntu:~/0x01$ 
	```
9. [There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important](9-print_last_digit.py) : Write a function that prints the last digit of a number.
	- Prototype: `def print_last_digit(number):`
	- Returns the value of the last digit
	- You are not allowed to import any module
	- You don’t need to understand `__import__`
10. [a + b](10-add.py) : Write a function that adds two integers and returns the result.
	- Prototype: `def add(a, b):`
	- Returns the value of `a + b`
	- You are not allowed to import any module
	- You don’t need to understand `__import__`
	```
	guillaume@ubuntu:~/0x01$ ./10-main.py
	3
	98
	98
	guillaume@ubuntu:~/0x01$ 
	```
11. [a ^ b](11-pow.py) : Write a function that computes a to the power of b and return the value.
	- Prototype: `def pow(a, b):`
	- Returns the value of `a ^ b`
	- You are not allowed to import any module
	- You don’t need to understand `__import__`
	```
	guillaume@ubuntu:~/0x01$ ./11-main.py
	4
	9604
	1
	0.0001
	-1024
	```
12. [Fizz Buzz](12-fizzbuzz.py) : Write a function that prints the numbers from 1 to 100 separated by a space.
	- For multiples of three print `Fizz` instead of the number and for multiples of five print `Buzz`.
	- For numbers which are multiples of both three and five print `FizzBuzz`.
	- Prototype: `def fizzbuzz():`
	- Each element should be followed by a space
	- You are not allowed to import any module
	- You don’t need to understand `__import__`
	```
	guillaume@ubuntu:~/0x01$ ./12-main.py | cat -e
	1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 
	31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 
	61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 
	91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz $
	guillaume@ubuntu:~/0x01$ 
	```
13. [Insert in sorted linked list](13-insert_number.c) :
	- Technical interview preparation:
	- You are not allowed to google anything
	- Whiteboard first
	- Write a function in C that inserts a number into a sorted singly linked list.
	- Prototype: `listint_t *insert_node(listint_t **head, int number);`
	- Return: the address of the new node, or `NULL` if it failed
14. [Smile in the mirror](100-print_tebahpla.py) : #advanced - Write a program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (z in lowercase and Y in uppercase), not followed by a new line.
	- You can only use one print function with string format
	- You can only use one loop in your code
	- You are not allowed to store characters in a variable
	- You are not allowed to import any module
	```
	guillaume@ubuntu:~/0x01$ ./100-print_tebahpla.py
	zYxWvUtSrQpOnMlKjIhGfEdCbAguillaume@ubuntu:~/0x01$
	```
15. [Remove at position](101-remove_char_at.py) : #advanced - Write a function that creates a copy of the string, removing the character at the position n (not the Python way, the “C array index”).
	- Prototype: `def remove_char_at(str, n):`
	- You are not allowed to import any module
	- You don’t need to understand `__import__`
	```
	guillaume@ubuntu:~/0x01$ cat 101-main.py
	#!/usr/bin/env python3
	remove_char_at = __import__('101-remove_char_at').remove_char_at

	print(remove_char_at("Best School", 3))
	print(remove_char_at("Chicago", 2))
	print(remove_char_at("C is fun!", 0))
	print(remove_char_at("School", 10))
	print(remove_char_at("Python", -2))

	guillaume@ubuntu:~/0x01$ ./101-main.py
	Bes School
	Chcago
 	is fun!
	School
	Python
	```
16. [ByteCode -> Python #2](102-magic_calculation.py) : #advanced - Write the Python function `def magic_calculation(a, b, c):` that does exactly the same as the following Python bytecode:
	```
  	3           0 LOAD_FAST                0 (a)
              	3 LOAD_FAST                1 (b)
              	6 COMPARE_OP               0 (<)
              	9 POP_JUMP_IF_FALSE       16

  	4          	12 LOAD_FAST                2 (c)
             	15 RETURN_VALUE

  	5     >>   	16 LOAD_FAST                2 (c)
            	19 LOAD_FAST                1 (b)
             	22 COMPARE_OP               4 (>)
             	25 POP_JUMP_IF_FALSE       36

  	6          	28 LOAD_FAST                0 (a)
             	31 LOAD_FAST                1 (b)
             	34 BINARY_ADD
             	35 RETURN_VALUE

  	7     >>   	36 LOAD_FAST                0 (a)
             	39 LOAD_FAST                1 (b)
             	42 BINARY_MULTIPLY
             	43 LOAD_FAST                2 (c)
             	46 BINARY_SUBTRACT
             	47 RETURN_VALUE
	```
	[tips - ByteCode](https://docs.python.org/3.4/library/dis.html)
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
