# Project: 0x0B. Python - Input/Output

## Resources

#### Read or watch:

* [7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
* [8.7. Predefined Clean-up Actions](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions)
* [Dive Into Python 3: Chapter 11. Files](./main/OceanofPDF.com_Dive_Into_Python_3_-_Mark_Pilgrim.pdf)
* [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
* [Learn to Program 8 : Reading / Writing Files](https://www.youtube.com/watch?v=EukxMIsNeqU)
* [Automate the Boring Stuff with Python](./main/Automate_the_Boring_Stuff_with_Python_2nd_Edition_Al_Sweigart_Z-Library.pdf)
* [All about py-file I/O](https://techvidvan.com/tutorials/python-file-read-write/)
## Learning Objectives

### General

* Why Python programming is awesome
* How to open a file
* How to write text in a file
* How to read the full content of a file 
* How to read a file line by line
* How to move the cursor in a file
* How to make sure a file is closed after using it
* What is and how to use the <code>with</code> statement
* What is <code>JSON</code>
* What is serialization
* What is deserialization
* How to convert a Python data structure to a JSON string 
* How to convert a JSON string to a Python data structure


## Description of what each file shows (Tasks):
* **main**	--- main folder that holds all test case files on how to use function
* Files that start with:

0. [Read file](./0-read_file.py) : Write a function that reads a text file (`UTF8`) and prints it to stdout:
	- Prototype: `def read_file(filename=""):`
	- You must use the `with` statement
	- You don’t need to manage `file permission` or `file doesn't exist` exceptions.
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x0B$ ./0-main.py
	We offer a truly innovative approach to education:
	focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

	A school every software engineer would have dreamt of!
	guillaume@ubuntu:~/0x0B$ 
	```
1. [Write to a file](./1-write_file.py) : Write a function that writes a string to a text file (`UTF8`) and returns the number of characters written:
	- Prototype: `def write_file(filename="", text=""):`
	- You must use the `with` statement
	- You don’t need to manage `file permission` exceptions.
	- Your function should create the file if doesn’t exist.
	- Your function should overwrite the content of the file if it already exists.
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x0B$ ./1-main.py
	29
	guillaume@ubuntu:~/0x0B$ cat my_first_file.txt
	This School is so cool!
	guillaume@ubuntu:~/0x0B$ 
	```
	- **No test case needed**
2. [Append to a file](./2-append_write.py) : Write a function that appends a string at the end of a text file (`UTF8`) and returns the number of characters added:
	- Prototype: def append_write(filename="", text=""):
	- If the file doesn’t exist, it should be created
	- You must use the with statement
	- You don’t need to manage file permission or file doesn't exist exceptions.
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x0B$ cat file_append.txt
	cat: file_append.txt: No such file or directory
	guillaume@ubuntu:~/0x0B$ ./2-main.py
	29
	guillaume@ubuntu:~/0x0B$ cat file_append.txt
	This School is so cool!
	guillaume@ubuntu:~/0x0B$ ./2-main.py
	29
	guillaume@ubuntu:~/0x0B$ cat file_append.txt
	This School is so cool!
	This School is so cool!
	guillaume@ubuntu:~/0x0B$ 
	```
	- **No test case needed**
3. [To JSON string](./3-to_json_string.py) : Write a function that returns the JSON representation of an object (string):
	- Prototype: `def to_json_string(my_obj):`
	- You don’t need to manage exceptions if the object can’t be serialized.
	```sh
	guillaume@ubuntu:~/0x0B$ ./3-main.py
	[1, 2, 3]
	<class 'str'>
	{"id": 12, "is_active": true, "name": "John", "info": {"average": 3.14, "age": 36}, "places": ["San Francisco", "Tokyo"]}
	<class 'str'>
	[TypeError] {3, 132} is not JSON serializable
	guillaume@ubuntu:~/0x0B$ 
	```
	- **No test cases needed**
4. [From JSON string to Object](./4-from_json_string.py) : Write a function that returns an object (Python data structure) represented by a JSON string:
	- Prototype: `def from_json_string(my_str):`
	- You don’t need to manage exceptions if the JSON string doesn’t represent an object.
	```sh
	guillaume@ubuntu:~/0x0B$ ./4-main.py
	[1, 2, 3]
	<class 'list'>
	{'id': 12, 'is_active': True, 'name': 'John', 'info': {'age': 36, 'average': 3.14}, 'places': ['San Francisco', 'Tokyo']}
	<class 'dict'>
	[ValueError] Expecting property name enclosed in double quotes: line 2 column 25 (char 25)
	guillaume@ubuntu:~/0x0B$ 
	```
	- **No test cases needed**
5. [Save Object to a file](./5-save_to_json_file.py) : Write a function that writes an Object to a text file, using a JSON representation:
	- Prototype: `def save_to_json_file(my_obj, filename):`
	- You must use the `with` statement
	- You don’t need to manage exceptions if the object can’t be serialized.
	- You don’t need to manage file permission exceptions.
	```sh
	guillaume@ubuntu:~/0x0B$ ./5-main.py
	[TypeError] {3, 132} is not JSON serializable
	guillaume@ubuntu:~/0x0B$ cat my_list.json ; echo ""
	[1, 2, 3]
	guillaume@ubuntu:~/0x0B$ cat my_dict.json ; echo ""
	{"name": "John", "places": ["San Francisco", "Tokyo"], "id": 12, "info": {"average": 3.14, "age": 36}, "is_active": true}
	guillaume@ubuntu:~/0x0B$ cat my_set.json ; echo ""

	guillaume@ubuntu:~/0x0B$ 
	```
	- **No test cases needed**
6. [Create object from a JSON file](./6-load_from_json_file.py) : Write a function that creates an Object from a “JSON file”:
	- Prototype: `def load_from_json_file(filename):`
	- You must use the `with` statement
	- You don’t need to manage exceptions if the JSON string doesn’t represent an object.
	- You don’t need to manage file permissions / exceptions.
	```sh
	guillaume@ubuntu:~/0x0B$ cat my_list.json ; echo ""
	[1, 2, 3]
	guillaume@ubuntu:~/0x0B$ cat my_dict.json ; echo ""
	{"name": "John", "places": ["San Francisco", "Tokyo"], "id": 12, "info": {"average": 3.14, "age": 36}, "is_active": true}
	guillaume@ubuntu:~/0x0B$ cat my_fake.json ; echo ""
	{"is_active": true, 12 }
	guillaume@ubuntu:~/0x0B$ ./6-main.py
	[1, 2, 3]
	<class 'list'>
	{'name': 'John', 'info': {'age': 36, 'average': 3.14}, 'id': 12, 'places': ['San Francisco', 'Tokyo'], 'is_active': True}
	<class 'dict'>
	[FileNotFoundError] [Errno 2] No such file or directory: 'my_set_doesnt_exist.json'
	[ValueError] Expecting property name enclosed in double quotes: line 1 column 21 (char 20)
	guillaume@ubuntu:~/0x0B$ 
	```
	- **No test cases needed**
7. [Load, add, save](./7-add_item.py) : Write a script that adds all arguments to a Python list, and then save them to a file:
	- You must use your function `save_to_json_file` from `5-save_to_json_file.py`
	- You must use your function `load_from_json_file` from `6-load_from_json_file.py`
	- The list must be saved as a JSON representation in a file named `add_item.json`
	- If the file doesn’t exist, it should be created
	- You don’t need to manage file permissions / exceptions.
	```sh
	guillaume@ubuntu:~/0x0B$ cat add_item.json
	cat: add_item.json: No such file or directory
	guillaume@ubuntu:~/0x0B$ ./7-add_item.py
	guillaume@ubuntu:~/0x0B$ cat add_item.json ; echo ""
	[]
	guillaume@ubuntu:~/0x0B$ ./7-add_item.py Best School
	guillaume@ubuntu:~/0x0B$ cat add_item.json ; echo ""
	["Best", "School"]
	guillaume@ubuntu:~/0x0B$ ./7-add_item.py 89 Python C
	guillaume@ubuntu:~/0x0B$ cat add_item.json ; echo ""
	["Best", "School", "89", "Python", "C"]
	guillaume@ubuntu:~/0x0B$ 
	```
	- **No test cases needed**
8. [Class to JSON](./8-class_to_json.py) : Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:
	- Prototype: `def class_to_json(obj):`
	- `obj` is an instance of a Class
	- All attributes of the `obj` Class are serializable: list, dictionary, string, integer and boolean
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x0B$ ./8-main.py 
	<class '8-my_class.MyClass'>
	[MyClass] John - 89
	<class 'dict'>
	{'name': 'John', 'number': 89}
	guillaume@ubuntu:~/0x0B$ 
	guillaume@ubuntu:~/0x0B$ ./8-main_2.py 
	<class '8-my_class_2.MyClass'>
	[MyClass] John - 4 => 1
	<class 'dict'>
	{'number': 4, '_MyClass__name': 'John', 'is_team_red': True, 'score': 1}
	guillaume@ubuntu:~/0x0B$
	```
	- **No test case needed**
9. [Student to JSON](./9-student.py) : Write a class `Student` that defines a student by:
	- Public instance attributes:
		- `first_name`
		- `last_name`
		- `age`
	- Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
	- Public method `def to_json(self):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`)
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x0B$ ./9-main.py 
	<class 'dict'>
	John
	<class 'str'>
	23
	<class 'int'>
	<class 'dict'>
	Bob
	<class 'str'>
	27
	<class 'int'>
	guillaume@ubuntu:~/0x0B$ 
	```
	- No test cases needed
10. [Student to JSON with filter](./10-student.py) : Write a class Student that defines a student by: (based on `9-student.py`)
	- Public instance attributes:
		- `first_name`
		- `last_name`
		- `age`
	- Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
	- Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`):
	- If `attrs` is a list of strings, only attribute names contained in this list must be retrieved.
	- Otherwise, all attributes must be retrieved
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x0B$ ./10-main.py 
	{'age': 23, 'last_name': 'Doe', 'first_name': 'John'}
	{'age': 27, 'first_name': 'Bob'}
	{'age': 27}
	guillaume@ubuntu:~/0x0B$
	```
	- **No test cases needed**
11. [Student to disk and reload](./11-student.py) : Write a class Student that defines a student by: (based on `10-student.py`)
	- Public instance attributes:
		- `first_name`
		- `last_name`
		- `age`
	- Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
	- Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`):
	- If `attrs` is a list of strings, only attribute names contained in this list must be retrieved.
	- Otherwise, all attributes must be retrieved
	- Public method `def reload_from_json(self, json):` that replaces all attributes of the `Student` instance:
		- You can assume `json` will always be a dictionary
		- A dictionary key will be the public attribute name
		- A dictionary value will be the value of the public attribute
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x0B$ ./11-main.py student.json
	Initial student:
	<11-student.Student object at 0x7f832826eda0>
	<class '11-student.Student'>
	<class 'dict'>
	John Doe 23
	{"last_name": "Doe", "first_name": "John", "age": 23}
	Saved to disk
	Fake student:
	<11-student.Student object at 0x7f832826edd8>
	<class '11-student.Student'>
	Fake Fake 89
	Load dictionary from file:
	<11-student.Student object at 0x7f832826edd8>
	<class '11-student.Student'>
	John Doe 23
	guillaume@ubuntu:~/0x0B$ cat student.json ; echo ""
	{"last_name": "Doe", "first_name": "John", "age": 23}
	guillaume@ubuntu:~/0x0B$ 
	```
	- **No test cases needed**
12. [Pascal's Triangle](./12-pascal_triangle.py) : 
- Technical interview preparation:
	- You are not allowed to google anything
	- Whiteboard first
- Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of `n`:
	- Returns an empty list if `n <= 0`
	- You can assume `n` will be always an integer
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x0B$ ./12-main.py
	[1]
	[1,1]
	[1,2,1]
	[1,3,3,1]
	[1,4,6,4,1]
	guillaume@ubuntu:~/0x0B$ 
	```
13. [Search and update](./100-append_after.py) : Write a function that inserts a line of text to a file, after each line containing a specific string (see example):
	- Prototype: `def append_after(filename="", search_string="", new_string=""):`
	- You must use the `with` statement
	- You don’t need to manage `file permission` or `file doesn't exist` exceptions.
	- You are not allowed to import any module
	```sh
	guillaume@ubuntu:~/0x0B$ cat append_after_100.txt
	At Holberton School,
	Python is really important,
	But it can be very hard if:
	- You don't get all Pythonic tricks
	- You don't have strong C knowledge.
	guillaume@ubuntu:~/0x0B$ ./100-main.py
	guillaume@ubuntu:~/0x0B$ cat append_after_100.txt
	At School,
	Python is really important,
	"C is fun!"
	But it can be very hard if:
	- You don't get all Pythonic tricks
	"C is fun!"
	- You don't have strong C knowledge.
	guillaume@ubuntu:~/0x0B$ ./100-main.py
	guillaume@ubuntu:~/0x0B$ cat append_after_100.txt
	At School,
	Python is really important,
	"C is fun!"
	"C is fun!"
	But it can be very hard if:
	- You don't get all Pythonic tricks
	"C is fun!"
	"C is fun!"
	- You don't have strong C knowledge.
	guillaume@ubuntu:~/0x0B$ 
	```
14. [Log parsing](./101-stats.py) : Write a script that reads stdin line by line and computes metrics:
	- Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
	- Each 10 lines and after a keyboard interruption (CTRL + C), prints those statistics since the beginning:
		- Total file size: File size: <total size>
		- where is the sum of all previous (see input format above)
		- Number of lines by status code:
			- possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
			- if a status code doesn’t appear, don’t print anything for this status code
			- format: <status code>: <number>
			- status codes should be printed in ascending order
	```sh
	guillaume@ubuntu:~/0x0B$ ./101-generator.py | ./101-stats.py 
	File size: 5213
	200: 2
	401: 1
	403: 2
	404: 1
	405: 1
	500: 3
	File size: 11320
	200: 3
	301: 2
	400: 1
	401: 2
	403: 3
	404: 4
	405: 2
	500: 3
	File size: 16305
	200: 3
	301: 3
	400: 4
	401: 2
	403: 5
	404: 5
	405: 4
	500: 4
	^CFile size: 17146
	200: 4
	301: 3
	400: 4
	401: 2
	403: 6
	404: 6
	405: 4
	500: 4
	Traceback (most recent call last):
	File "./101-stats.py", line 15, in <module>
	Traceback (most recent call last):
	File "./101-generator.py", line 8, in <module>
		for line in sys.stdin:
	KeyboardInterrupt
		sleep(random.random())
	KeyboardInterrupt
	guillaume@ubuntu:~/0x0B$ 
	```
	- **No test cases needed**

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
