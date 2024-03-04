# Project: 0x15. JavaScript - Web jQuery

![did_sum1_say_jquery](./did_someone_say_jquery.jpg)

## Resources

### Read or watch:-

- [What is JavaScript?](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
- [Selector](https://jquery-tutorial.net/selectors/using-elements-ids-and-classes/)
- [Get and set content](https://jquery-tutorial.net/dom-manipulation/getting-and-setting-content/)
- [Manipulate CSS classes](https://jquery-tutorial.net/dom-manipulation/getting-and-setting-css-classes/)
- [Manipulate DOM elements](https://jquery-tutorial.net/dom-manipulation/the-append-and-prepend-methods/)
- [API](https://oscarotero.com/jquery/)
- [Introduction](https://jquery-tutorial.net/ajax/introduction/)
- [GET & POST request](https://jquery-tutorial.net/ajax/the-get-and-post-methods/)
- [JQuery Ajax Tutorial #1 - Using AJAX & API's](https://www.youtube.com/watch?v=fEYx8dQr_cQ)
- [What went wrong? Troubleshooting JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong)
- [JQuery](https://jquery.com/)
- [JQuery API](https://api.jquery.com/)
- [JQuery Ajax](https://learn.jquery.com/ajax/)

## Learning Objectives

### General

- Why JQuery make front-end programming so easy (don’t forget to tweet today, with the hashtag #ilovejquery :))
- How to select HTML elements in JavaScript
- How to select HTML elements with JQuery
- What are differences between `ID`, `class` and `tag name` selectors
- How to modify an HTML element style
- How to get and update an HTML element content
- How to modify the DOM
- How to make a `GET` request with JQuery Ajax
- How to make a `POST` request with JQuery Ajax
- How to listen/bind to DOM events

## Tasks

0. [No JQuery](./0-script.js) :

Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):

- You must use `document.querySelector` to select the HTML tag
- You can’t use the JQuery API
- Please test with this HTML file in your browser: [0-main.html](./0-main.html)

1. [With JQuery](./1-script.js) :

Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):

- You can’t use `document.querySelector` to select the HTML tag
- You must use the JQuery API
- Please test with this HTML file in your browser: [1-main.html](./1-main.html)

2. [Click and turn red](./2-script.js) :

Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`) when the user clicks on the tag `DIV#red_header`

- You can’t use `document.querySelector` to select the HTML tag
- You must use the JQuery API
- Please test with this HTML file in your browser: [2-main.html](./2-main.html)

3. [Add `.red` class](./3-script.js) :

Write a JavaScript script that adds the class red to the `<header>` element when the user clicks on the tag `DIV#red_header`

- You can’t use `document.querySelector` to select the HTML tag
- You must use the JQuery API
- Please test with this HTML file in your browser: [3-main.html](./3-main.html)

4. [Toggle classes](./4-script.js) :

Write a JavaScript script that toggles the class of the `<header>` element when the user clicks on the tag DIV#toggle_header:

- The `<header>` element must always have one class: `red` or `green`, never both in the same time and never empty.
- If the current class is `red`, when the user click on `DIV#toggle_header`, the class must be updated to `green` ; and the reverse.
- You can’t use `document.querySelector` to select the HTML tag
- You must use the JQuery API
- Please test with this HTML file in your browser: [4-main.html](./4-main.html)

5. [List of elements](./5-script.js) :

Write a JavaScript script that adds a `<li>` element to a list when the user clicks on the tag `DIV#add_item`:

- The new element must be: `<li>Item</li>`
- The new element must be added to `UL.my_list`
- You can’t use `document.querySelector` to select the HTML tag
- You must use the JQuery API
- Please test with this HTML file in your browser: [5-main.html](./5-main.html)

6. [Change the text](./6-script.js) :

Write a JavaScript script that updates the text of the `<header>` element to New Header!!! when the user clicks on `DIV#update_header`

- You can’t use `document.querySelector` to select the HTML tag
- You must use the JQuery API
- Please test with this HTML file in your browser: [6-main.html](./6-main.html)

7. [Star wars character](./7-script.js) :

Write a JavaScript script that fetches the character `name` from this URL: `https://swapi-api.alx-tools.com/api/people/5/?format=json`

- The name must be displayed in the HTML tag `DIV#character`
- You can’t use `document.querySelector` to select the HTML tag
- You must use the JQuery API
- Please test with this HTML file in your browser: [7-main.html](./7-main.html)

8. [Star Wars movies](./8-script.js) :

Write a JavaScript script that fetches and lists the `title` for all movies by using this URL: `https://swapi-api.alx-tools.com/api/films/?format=json`

- All movie titles must be list in the HTML tag `UL#list_movies`
- You can’t use `document.querySelector` to select the HTML tag
- You must use the JQuery API
- Please test with this HTML file in your browser: [8-main.html](./8-main.html)

9. [Say Hello!](./9-script.js) :

Write a JavaScript script that fetches from `https://hellosalut.stefanbohacek.dev/?lang=fr` and displays the value of hello from that fetch in the HTML tag DIV#hello.

- The translation of “hello” must be displayed in the HTML tag `DIV#hello`
- You can’t use `document.querySelector` to select the HTML tag
- You must use the JQuery API
- Your script must work when it is imported from the `<head>` tag
- Please test with this HTML file in your browser: [9-main.html](./9-main.html)

10. [No jQuery - document loaded](./100-script.js) :

Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):

- You must use `document.querySelector` to select the HTML tag
- You can’t use the jQuery API
- Note: Your script must be imported from the `<head>` tag, not at the end of the HTML
- Please test with this HTML file in your browser: [100-main.html](./100-main.html)

11. [List, Add, Remove](./101-script.js) :

Write a JavaScript script that adds, removes and clears LI elements from a list when the user clicks:

- The new element must be: `<li>Item</li>`
- The new element must be added to `UL.my_list`
- When the user clicks on `DIV#add_item`: a new element is added to the list
- When the user clicks on `DIV#remove_item`: the last element is removed from the list
- When the user clicks on `DIV#clear_list`: all elements of the list are removed
- You can’t use `document.querySelector` to select the HTML tag
- You must use the JQuery API
- You script must work when it imported from the `HEAD` tag
- Please test with this HTML file in your browser: [101-main.html](./101-main.html)

12. [Say hello to everybody!](./102-script.js) :

Write a JavaScript script that fetches and prints how to say “Hello” depending on the language

- You should use this API service: `https://www.fourtonfish.com/hellosalut/hello/`
- The language code will be the value entered in the tag `INPUT#language_code` (ex: `es`, `fr`, `en` etc.)
- The translation must be fetched when the user clicks on `INPUT#btn_translate`
- The translation of “Hello” must be displayed in the HTML tag `DIV#hello`
- You can’t use `document.querySelector` to select the HTML tag
- You must use the JQuery API
- You script must work when imported from the `<head>` tag
- Please test with this HTML file in your browser: [102-main.html](./102-main.html)

13. [And press ENTER](./103-scripts) :

Write a JavaScript script that fetches and prints how to say “Hello” depending on the language

You should use this API service: `https://www.fourtonfish.com/hellosalut/hello/`
The language code will be the value entered in the tag `INPUT#language_code` (ex: `es`, `fr`, `en` etc.)
The translation must be fetched when the user clicks on `INPUT#btn_translate` OR presses `ENTER` when the focus is on `INPUT#language_code`
The translation of “Hello” must be displayed in the HTML tag `DIV#hello`
You can’t use `document.querySelector` to select the HTML tag
You must use the JQuery API
You script must work when imported from the `<head>` tag
Please test with this HTML file in your browser: [103-main.html](./103-main.html)

---

### Environment

- Language: Javascript, jQuery v3.2.1
  - OS: Ubuntu 20.04 LTS
  - Style guidelines:
    - [Javascript Semistandard](https://github.com/standard/semistandard) `sudo npm install semistandard --global`
  - [Install Semistandard - Note](../0x12-javascript-warm_up/README.md)
    - [Airbnb Javascript Style Guide](https://github.com/airbnb/javascript)

---