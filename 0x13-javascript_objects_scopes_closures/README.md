# Project: 0x13. JavaScript - Objects, Scopes and Closures

## Resources

### Read or watch:

- [JavaScript object basics](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Basics)
- [Object-oriented JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript)
- [Class - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
- [super - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super)
- [extends - ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends)
- [Object prototypes](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes)
- [Inheritance in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript)
- [Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)
- [this/self](https://alistapart.com/article/getoutbindingsituations/)
- [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

## Learning Objectives

### General

- Why JavaScript programming is amazing
- How to create an object in JavaScript
- What <code>this</code> means
- What <code>undefined</code> means
- Why the variable type and scope is important
- What is a closure
- What is a prototype
- How to inherit an object from another

## Description of each files shows (Tasks):

- main - help folder to hold main.js files provided by ALX and or images to make README better.

0. [Rectangle #0](./0-rectangle.js) :

Write an empty class `Rectangle` that defines a rectangle:

- You must use the `class` notation for defining your class

```sh
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$ ./0-main.js
Rectangle {}
[Function: Rectangle]
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$
```

1. [Rectangle #1](./1-rectangle.js) :

Write a class `Rectangle` that defines a rectangle:

- You must use the `class` notation for defining your class
- The constructor must take 2 arguments `w` and `h`
- Initialize the instance attribute `width` with the value of `w`
- Initialize the instance attribute `height` with the value of `h`

```sh
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$ ./1-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle { width: 2, height: -3 }
2
-3
Rectangle { width: 2, height: undefined }
2
undefined
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$
```

2. [Rectangle #2](./2-rectangle.js) :

Write a class Rectangle that defines a rectangle:

- You must use the class notation for defining your class
- The constructor must take 2 arguments `w` and `h`
- Initialize the instance attribute `width` with the value of `w`
- Initialize the instance attribute `height` with the value of `h`
- If `w` or `h` is equal to 0 or not a positive integer, create an empty object

```sh
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$ ./2-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$
```

3. [Rectangle #3](./3-rectangle.js) :

Write a class `Rectangle` that defines a rectangle:

- You must use the `class` notation for defining your class
- The constructor must take 2 arguments: `w` and `h`
- Initialize the instance attribute `width` with the value of `w`
- Initialize the instance attribute `height` with the value of `h`
- If `w` or `h` is equal to `0` or not a positive integer, create an empty object
- Create an instance method called `print()` that prints the rectangle using the character `X`

```sh
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$ ./3-main.js
XX
XX
XX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$
```

4. [Rectangle #4](./4-rectangle.js) :

Write a class `Rectangle` that defines a rectangle:

- You must use the `class` notation for defining your class
- The constructor must take 2 arguments: `w` and `h`
- Initialize the instance attribute `width` with the value of `w`
- Initialize the instance attribute `height` with the value of `h`
- If `w` or `h` is equal to 0 or not a positive integer, create an empty object
- Create an instance method called `print()` that prints the rectangle using the character `X`
- Create an instance method called `rotate()` that exchanges the `width` and the `height` of the rectangle
- Create an instance method called `double()` that multiples the `width` and the `height` of the rectangle by 2

```sh
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$ semistandard 4-rectangle.js
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$ ./4-main.js
Normal:
XX
XX
XX
Double:
XXXX
XXXX
XXXX
XXXX
XXXX
XXXX
Rotate:
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$
```

5. [Square #0](./5-square.js) :

Write a class `Square` that defines a square and inherits from `Rectangle` of `4-rectangle.js`:

- You must use the `class` notation for defining your class and `extends`
- The constructor must take 1 argument: `size`
- The constructor of `Rectangle` must be called (by using `super()`)

```sh
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$ ./5-main.js
XXXX
XXXX
XXXX
XXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$
```

6. [Square #1](./6-square.js) :

Write a class `Square` that defines a square and inherits from Sq`uare of `5-square.js`:

- You must use the `class` notation for defining your class and `extends`
- Create an instance method called `charPrint(c)` that prints the rectangle using the character `c`
  - If `c` is `undefined`, use the character `X`

```sh
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$ ./6-main.js
XXXX
XXXX
XXXX
XXXX
CCCC
CCCC
CCCC
CCCC
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$
```

7. [Occurrences](./7-occurrences.js) :

Write a function that returns the number of occurrences in a list:

- Prototype: `exports.nbOccurences = function (list, searchElement)`

```sh
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$ ./7-main.js
1
4
2
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$
```

8. [Esrever](./8-esrever.js) :

Write a function that returns the reversed version of a list:

- Prototype: `exports.esrever = function (list)`
- You are not allow to use the built-in method `reverse`

```sh
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$ ./8-main.js
[ 5, 4, 3, 2, 1 ]
[ 'String', { id: 12 }, 89, 'School' ]
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$ ./8-main.js
[ 5, 4, 3, 2, 1 ]
[ 'String', { id: 12 }, 89, 'School' ]
5
```

9. [Log me](./9-logme.js) :

Write a function that prints the number of arguments already printed and the new argument value. (see example below)

- Prototype: `exports.logMe = function (item)`
- Output format: `<number arguments already printed>: <current argument value>`

```sh
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$ ./9-main.js
0: Hello
1: Best
2: School
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$
```

10. [Number conversion](./10-converter.js) :

Write a function that converts a number from base 10 to another base passed as argument:

- Prototype: `exports.converter = function (base)`
- You are not allowed to import any file
- You are not allowed to declare any new variable (var, let, etc..)

```sh
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$ ./10-main.js
2
12
89
2
c
59
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$
```

11. [Factor Index](./100-map.js) :

Write a script that imports an array and computes a new array.

- Your script must import `list` from the file `100-data.js`
- You must use a `map`. [Tips](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map?v=control)
- A new list must be created with each value equal to the value of the initial list, multipled by the index in the list
- Print both the initial list and the new list

```sh
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$ ./100-map.js 
[ 1, 2, 3, 4, 5 ]
[ 0, 2, 6, 12, 20 ]
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$ 
```

12. [Sorted Occurences](./101-sorted.js) :

Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

- Your script must import `dict` from the file `101-data.js`
- In the new dictionary:
- A key is a number of occurrences
- A value is the list of user ids
- Print the new dictionary at the end

```sh
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$ ./101-sorted.js 
{ '1': [ '89', '91', '93' ], '2': [ '90', '94' ], '3': [ '92' ] }
```

13. [Concat files](./102-concat.js) :

Write a script that concats 2 files.

- The first argument is the file path of the first source file
- The second argument is the file path of the second source file
- The third argument is the file path of the destination

```sh
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$ cat fileA
C is fun!
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$ cat fileB
Python is cool!!!
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$ ./102-concat.js fileA fileB new_file
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$ cat new_file
C is fun!
Python is cool!!!
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$ 
```

---

### Environment

- Language: Javascript, Node v20.10.0
  - OS: Ubuntu 20.04 LTS
  - Style guidelines:
    - [Javascript Semistandard](https://github.com/standard/semistandard) `sudo npm install semistandard --global`
	- [Install Semistandard - Note](../0x12-javascript-warm_up/README.md)
    - [Airbnb Javascript Style Guide](https://github.com/airbnb/javascript)

---

## Author

