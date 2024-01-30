# Project: 0x11. Python - Network #1

## Resources

### Read or watch:-

- [HOWTO Fetch Internet Resources Using urllib Package](https://docs.python.org/3/howto/urllib2.html)
- [Quickstart with Requests package](https://requests.readthedocs.io/en/latest/)
- [Requests package](https://pypi.org/project/requests/)

## Learning Objectives

### General

- How to fetch internet resources with the Python package `urllib`
- How to decode `urllib` body response
- How to use the Python package `requests` #requestsiswaysimplerthanurllib
- How to make HTTP `GET` request
- How to make HTTP `POST`/`PUT`/etc. request
- How to fetch JSON resources
- How to manipulate data from an external service

## Tasks

0. [What's my status? #0](./0-hbtn_status.py) :

Write a Python script that fetches `https://alx-intranet.hbtn.io/status`

- You must use the package `urllib`
- You are not allowed to import any packages other than `urllib`
- The body of the response must be displayed like the following example (tabulation before `-`)
- You must use a `with` statement

```sh
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x11-python-network_1$ ./0-hbtn_status.py | cat -e
Body response:$
        - type: <class 'bytes'>$
        - content: b'OK'$
        - utf8 content: OK$
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x11-python-network_1$ 
```

1. [Response header value #0](./1-hbtn_header.py) :

Write a Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response.

- You must use the packages `urllib` and `sys`
- You are not allow to import packages other than `urllib` and `sys`
- The value of this variable is different for each request
- You don’t need to check arguments passed to the script (number or type)
- You must use a `with` statement

```sh
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x11-python-network_1$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
377b805d-df8c-4449-b756-dea1a4d19b6a
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x11-python-network_1$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
38a5cace-ff33-4e3f-9d50-281dae0e21b4
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x11-python-network_1$ 
```

2. [POST an email #0](./2-post_email.py) :

Write a Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`)

- The email must be sent in the `email` variable
- You must use the packages `urllib` and `sys`
- You are not allowed to import packages other than `urllib` and `sys`
- You don’t need to check arguments passed to the script (number or type)
- You must use the `with` statement

Please test your script in the sandbox provided, using the web server running on port 5000

```sh
root@6bacb30be86d:/alx-higher_level_programming/0x11-python-network_1# ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
root@6bacb30be86d:/alx-higher_level_programming/0x11-python-network_1# 
```

3. [Error code #0](./3-error_code.py) :

Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`).

- You have to manage `urllib.error.HTTPError` exceptions and print: `Error code:` followed by the HTTP status code
- You must use the packages `urllib` and `sys`
- You are not allowed to import other packages than `urllib` and `sys`
- You don’t need to check arguments passed to the script (number or type)
- You must use the `with` statement

Please test your script in the sandbox provided, using the web server running on port 5000

```sh
root@6bacb30be86d:/alx-higher_level_programming/0x11-python-network_1# ./3-error_code.py http://0.0.0.0:5000
Index
root@6bacb30be86d:/alx-higher_level_programming/0x11-python-network_1# ./3-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
root@6bacb30be86d:/alx-higher_level_programming/0x11-python-network_1# ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
root@6bacb30be86d:/alx-higher_level_programming/0x11-python-network_1# ./3-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
root@6bacb30be86d:/alx-higher_level_programming/0x11-python-network_1#
```

4. [What's my status? #1](./4-hbtn_status.py) :

Write a Python script that fetches `https://alx-intranet.hbtn.io/status`

- You must use the package `requests`
- You are not allow to import packages other than `requests`
- The body of the response must be display like the following example (tabulation before `-`)

```sh
root@6bacb30be86d:/alx-higher_level_programming/0x11-python-network_1# ./4-hbtn_status.py | cat -e
Body response:$
        - type: <class 'str'>$
        - content: OK$
root@6bacb30be86d:/alx-higher_level_programming/0x11-python-network_1# 
```

5. [Response header value #1](./5-hbtn_header.py) :

Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header

- You must use the packages `requests` and `sys`
- You are not allow to import other packages than `requests` and `sys`
- The value of this variable is different for each request
- You don’t need to check script arguments (number and type)

```sh
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x11-python-network_1$ ./5-hbtn_header.py https://alx-intranet.hbtn.io
3d285023-5df5-400e-b28f-c091ed0be54a
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x11-python-network_1$ 
```

6. [POST an email #1](./6-post_email.py) :

Write a Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response.

- The email must be sent in the variable `email`
- You must use the packages `requests` and `sys`
- You are not allowed to import packages other than `requests` and `sys`
- You don’t need to error check arguments passed to the script (number or type)

Please test your script in the sandbox provided, using the web server running on port 5000

```sh
root@6bacb30be86d:/alx-higher_level_programming/0x11-python-network_1# ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
root@6bacb30be86d:/alx-higher_level_programming/0x11-python-network_1# 
```

7. [Error code #1](./7-error_code.py) :

Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.

- If the HTTP status code is greater than or equal to 400, print: `Error code:` followed by the value of the HTTP status code
- You must use the packages `requests` and `sys`
- You are not allowed to import packages other than `requests` and `sys`
- You don’t need to check arguments passed to the script (number or type)

Please test your script in the sandbox provided, using the web server running on port 5000

```sh
root@6bacb30be86d:/alx-higher_level_programming/0x11-python-network_1# ./7-error_code.py http://0.0.0.0:5000
Index
root@6bacb30be86d:/alx-higher_level_programming/0x11-python-network_1# ./7-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
root@6bacb30be86d:/alx-higher_level_programming/0x11-python-network_1# ./7-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
root@6bacb30be86d:/alx-higher_level_programming/0x11-python-network_1# ./7-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
root@6bacb30be86d:/alx-higher_level_programming/0x11-python-network_1# 
```

8. [Search API](./8-json_api.py) :

Write a Python script that takes in a letter and sends a `POST` request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.

- The letter must be sent in the variable `q`
- If no argument is given, set `q=""`
- If the response body is properly JSON formatted and not empty, display the `id` and `name` like this: `[<id>] <name>`
Otherwise:
  - Display `Not a valid JSON` if the JSON is invalid
  - Display `No result` if the JSON is empty
- You must use the package `requests` and `sys`
- You are not allowed to import packages other than `requests` and `sys`

Please test your script in the sandbox provided, using the web server running on port 5000. All JSON generated by this server are random.

```sh
root@6bacb30be86d:/alx-higher_level_programming/0x11-python-network_1# ./8-json_api.py 
No result
root@6bacb30be86d:/alx-higher_level_programming/0x11-python-network_1# ./8-json_api.py a
[9180] aglqtnjclsa
root@6bacb30be86d:/alx-higher_level_programming/0x11-python-network_1# ./8-json_api.py 2
No result
root@6bacb30be86d:/alx-higher_level_programming/0x11-python-network_1# ./8-json_api.py b
[8756] bqwlbhfpqib
root@6bacb30be86d:/alx-higher_level_programming/0x11-python-network_1# ./8-json_api.py c
[8848] cpiljnltmie
root@6bacb30be86d:/alx-higher_level_programming/0x11-python-network_1# 
```

9. [My GitHub!](./10-my_github.py) :

Write a Python script that takes your GitHub credentials (username and password) and uses the [GitHub API](https://docs.github.com/en/rest/users?apiVersion=2022-11-28) to display your `id`

- You must use [Basic Authentication](https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api?apiVersion=2022-11-28) with a [personal access token as password](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) to access to your information (only `read:user` permission is needed)
- The first argument will be your `username`
- The second argument will be your `password` (in your case, a personal access token as password)
- You must use the package `requests` and `sys`
- You are not allowed to import packages other than `requests` and `sys`
- You don’t need to check arguments passed to the script (number or type)

```sh
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x11-python-network_1$ ./10-my_github.py AyomideKayode my_personal_access_token
117745553
cobby@cobby-VirtualBox:~/alx-higher_level_programming/0x11-python-network_1$ 
```

10. [Time for an interview!](./100-github_commits.py) :

The Holberton School staff evaluates candidates applying for a back-end position with multiple technical challenges, like this one:

```sh
Please list 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
```

Write a Python script that takes 2 arguments in order to solve this challenge.

- The first argument will be the `repository name`
- The second argument will be the `owner name`
- You must use the packages `requests` and `sys`
- You are not allowed to import packages other than `requests` and `sys`
- You don’t need to check arguments passed to the script (number or type)

Only 17% of applicants for a backend position at Holberton finished this task in less than 15 minutes.

```sh
guillaume@ubuntu:~/0x11$ ./100-github_commits.py rails rails
3b5a6dfb18f33c373a89760c60d741f34206f23b: Jon Moss
f785ad786ae49dd6f7a2f1d77c44ea17008c6656: Jon Moss
bb13c37fefdc8b5699918b38eff84751c2899ad5: Rafael França
f5d880866917724217eae9785a3ccd3f806c5aaf: Rafael França
0da696a5e3cee87a996a020b664caa1eabd66220: Ryuta Kamizono
24eb450d7599bab1f5863e0578a21c65ca42a915: Matthew Draper
668f8691f1017042e238497d1a5b7b8bf1c43819: Matthew Draper
a76f5189f6cec4b3e6d9035e2b55dcda6050dfdb: Ryuta Kamizono
28079868d0e70bdac80c76cf806afd517edfe1e7: Rafael França
8f0d8551893789f26e5d6b82ccef00779296818f: Rafael Mendonça França
guillaume@ubuntu:~/0x11$ 
```

Be careful: only 60 requests by hour by IP for unauthenticated requests [Rate limit](https://docs.github.com/en/rest?apiVersion=2022-11-28)

---

### Environment

- Language: Python 3.4.3
  - OS: Ubuntu 20.04 LTS
  - Compiler: python3
  - Style guidelines:
    - [PEP 8 (version 1.7)](https://www.python.org/dev/peps/pep-0008/)

---

## Author

- **<em>Website</em>** - [Ayomide Kayode](https://github.com/AyomideKayode)
- **<em>ALX Software Engineering Program</em>** - [ALX_AFRICA](https://www.alxafrica.com/programmes/)
- **<em>Twitter</em>** - [@kazzy_wiz](https://www.twitter.com/kazzy_wiz)