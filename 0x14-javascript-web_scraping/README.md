# Project: 0x14. JavaScript - Web scraping

## Resources

### Read or watch:-

- [Working with JSON data](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)
- [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://medium.com/@vietkieutie/the-workflow-of-accessing-the-attributes-of-a-simply-created-json-object-82a5b33e2319)
- [request module](https://github.com/request/request)
- [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

## Learning Objectives

### General

- Why JavaScript programming is amazing
- How to manipulate JSON data
- How to use `request` and fetch API
- How to read and write a file using `fs` module

### More Info

#### Install Node 14

```sh
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

#### Install semi-standard

[Documentation](https://github.com/standard/semistandard)

```sh
$ sudo npm install semistandard --global
```

#### Install `request` module and use it

[Documentation](https://github.com/request/request)

```sh
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

**Notes**: Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).

## Tasks

0. [Readme](./0-readme.js) :

Write a script that reads and prints the content of a file.

- The first argument is the file path
- The content of the file must be read in `utf-8`
- If an error occurred during the reading, print the error object

```sh
cobby@ubuntu:~/alx-higher_level_programming/0x14-javascript-web_scraping$ ./0-readme.js cisfun
C is super fun!

cobby@ubuntu:~/alx-higher_level_programming/0x14-javascript-web_scraping$ ./0-readme.js doesntexist
{ [Error: ENOENT: no such file or directory, open 'doesntexist']
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
cobby@ubuntu:~/alx-higher_level_programming/0x14-javascript-web_scraping$
```

1. [Write me](./1-writeme.js) :

Write a script that writes a string to a file.

- The first argument is the file path
- The second argument is the string to write
- The content of the file must be written in `utf-8`
- If an error occurred during while writing, print the error object

```sh
cobby@ubuntu:~/alx-higher_level_programming/0x14-javascript-web_scraping$ ./1-writeme.js my_file.txt "Python is cool"
cobby@ubuntu:~/alx-higher_level_programming/0x14-javascript-web_scraping$ cat my_file.txt
Python is coolcobby@ubuntu:~/alx-higher_level_programming/0x14-javascript-web_scraping$ cat my_file.txt ; echo ""
Python is cool
cobby@ubuntu:~/alx-higher_level_programming/0x14-javascript-web_scraping$
```

2. [Status code](./2-statuscode.js) :

Write a script that display the status code of a `GET` request.

- The first argument is the URL to request (`GET`)
- The status code must be printed like this: `code: <status code>`
- You must use the module `request`

```sh
cobby@ubuntu:~/alx-higher_level_programming/0x14-javascript-web_scraping$ ./2-statuscode.js https://alx-intranet.hbtn.io/status
code: 200
cobby@ubuntu:~/alx-higher_level_programming/0x14-javascript-web_scraping$
```

3. [Star wars movie title](./3-starwars_title.js) :

Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

- The first argument is the movie ID
- You must use the [Star wars API](https://swapi-api.alx-tools.com/) with the endpoint `https://swapi-api.alx-tools.com/api/films/:id`
- You must use the module request

```sh
cobby@ubuntu:~/alx-higher_level_programming/0x14-javascript-web_scraping$ ./3-starwars_title.js 1
A New Hope
cobby@ubuntu:~/alx-higher_level_programming/0x14-javascript-web_scraping$ ./3-starwars_title.js 5
Attack of the Clones
cobby@ubuntu:~/alx-higher_level_programming/0x14-javascript-web_scraping$
```

4. [Star wars Wedge Antilles](./4-starwars_count.js) :

Write a script that prints the number of movies where the character “Wedge Antilles” is present.

- The first argument is the API URL of the [Star wars API](https://swapi-api.alx-tools.com/): `https://swapi-api.alx-tools.com/api/films/`
- Wedge Antilles is character ID `18` - your script must use this ID for filtering the result of the API
- You must use the module `request`

```sh
cobby@ubuntu:~/alx-higher_level_programming/0x14-javascript-web_scraping$ ./4-starwars_count.js https://swapi-api.alx-tools.com/api/films
3
```

5. [Loripsum](./5-request_store.js) :

Write a script that gets the contents of a webpage and stores it in a file.

- The first argument is the URL to request
- The second argument the file path to store the body response
- The file must be UTF-8 encoded
- You must use the module `request`

```sh
guillaume@ubuntu:~/0x14$ ./5-request_store.js http://loripsum.net/api loripsum
guillaume@ubuntu:~/0x14$ cat loripsum
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Haec quo modo conveniant, non sane intellego. Nam memini etiam quae nolo, oblivisci non possum quae volo. Te enim iudicem aequum puto, modo quae dicat ille bene noris. Terram, mihi crede, ea lanx et maria deprimet. Deinde prima illa, quae in congressu solemus: Quid tu, inquit, huc? Hoc etsi multimodis reprehendi potest, tamen accipio, quod dant. </p>

<p>Ad eos igitur converte te, quaeso. Pudebit te, inquam, illius tabulae, quam Cleanthes sane commode verbis depingere solebat. Sic enim censent, oportunitatis esse beate vivere. Quo studio Aristophanem putamus aetatem in litteris duxisse? Aeque enim contingit omnibus fidibus, ut incontentae sint. Ut aliquid scire se gaudeant? Qui enim existimabit posse se miserum esse beatus non erit. Putabam equidem satis, inquit, me dixisse. </p>

<p>Duo Reges: constructio interrete. Quid ei reliquisti, nisi te, quoquo modo loqueretur, intellegere, quid diceret? Quis animo aequo videt eum, quem inpure ac flagitiose putet vivere? Illud non continuo, ut aeque incontentae. Illa videamus, quae a te de amicitia dicta sunt. At ille pellit, qui permulcet sensum voluptate. Tamen aberramus a proposito, et, ne longius, prorsus, inquam, Piso, si ista mala sunt, placet. </p>

<p>Non enim, si omnia non sequebatur, idcirco non erat ortus illinc. Nos cum te, M. Quem si tenueris, non modo meum Ciceronem, sed etiam me ipsum abducas licebit. Apparet statim, quae sint officia, quae actiones. Ergo instituto veterum, quo etiam Stoici utuntur, hinc capiamus exordium. Eadem nunc mea adversum te oratio est. Quid, si etiam iucunda memoria est praeteritorum malorum? Hoc enim constituto in philosophia constituta sunt omnia. </p>

guillaume@ubuntu:~/0x14$
```

6. [How many completed?](./6-completed_tasks.js) :

Write a script that computes the number of tasks completed by user id.

- The first argument is the API URL: `https://jsonplaceholder.typicode.com/todos`
- Only print users with completed task
- You must use the module `request`

```sh
cobby@ubuntu:~/alx-higher_level_programming/0x14-javascript-web_scraping$ ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
{ '1': 11,
  '2': 8,
  '3': 7,
  '4': 6,
  '5': 12,
  '6': 6,
  '7': 9,
  '8': 11,
  '9': 8,
  '10': 12 }
cobby@ubuntu:~/alx-higher_level_programming/0x14-javascript-web_scraping$
```

7. [Who was playing in this movie?](./100-starwars_characters.js) :

Write a script that prints all characters of a Star Wars movie:

- The first argument is the Movie ID - example: 3 = “Return of the Jedi”
- Display one character name by line
- You must use the `Star wars API`
- You must use the module `request`

```sh
cobby@ubuntu:~/alx-higher_level_programming/0x14-javascript-web_scraping$ ./100-starwars_characters.js 3
cobby@ubuntu:~/alx-higher_level_programming/0x14-javascript-web_scraping$ ./100-starwars_characters.js 3
C-3PO
Obi-Wan Kenobi
Leia Organa
Darth Vader
R2-D2
Chewbacca
Han Solo
Jabba Desilijic Tiure
Yoda
Luke Skywalker
Palpatine
Wedge Antilles
Lando Calrissian
Boba Fett
Ackbar
Arvel Crynyd
Nien Nunb
Wicket Systri Warrick
Mon Mothma
Bib Fortuna
cobby@ubuntu:~/alx-higher_level_programming/0x14-javascript-web_scraping$
```

8. [Right Order](./101-starwars_characters.js) :

Write a script that prints all characters of a Star Wars movie:

- The first argument is the Movie ID - example: 3 = “Return of the Jedi”
- Display one character name by line in the same order of the list “characters” in the /films/ response
- You must use the Star wars API
- You must use the module `request`

```sh
cobby@ubuntu:~/alx-higher_level_programming/0x14-javascript-web_scraping$ ./101-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
cobby@ubuntu:~/alx-higher_level_programming/0x14-javascript-web_scraping$ semistandard 101-starwars_characters.js
cobby@ubuntu:~/alx-higher_level_programming/0x14-javascript-web_scraping$
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
