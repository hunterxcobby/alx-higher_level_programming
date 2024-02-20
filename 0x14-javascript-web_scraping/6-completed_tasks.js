#!/usr/bin/node

// Require the 'request' module
const request = require('request');

// Get the URL from the command line arguments
const apiUrl = process.argv[2];

// Make a request to the specified URL
request(apiUrl, (error, response, body) => {
  if (error) { // check for errors in the request
    console.error(error);
  } else if (response.statusCode === 200) {
    // If statuscode is 200 (OK), proceed

    const todos = JSON.parse(body); // parse the JSON response body
    // create empty dict to store user IDs and their completed tasks count
    const completedTasksByUser = {};

    // Iterate over each todos
    for (const i in todos) {
      // check if todo is completed
      if (todos[i].completed) {
        // if userID is not in dict, initialize it with 1
        if (completedTasksByUser[todos[i].userId] === undefined) {
          completedTasksByUser[todos[i].userId] = 1;
        } else {
          // if userID already in dict, increment by 1
          completedTasksByUser[todos[i].userId]++;
        }
      }
    }
    // output d dictionary containing user IDs and their completed todos count
    console.log(completedTasksByUser);
  } else {
    // if the response status code is not 200, output an error message
    console.log('Error code: ' + response.statusCode);
  }
});

// As an alternative, flagged by checker though. Different output, same result
// todos.forEach((todo) => {
//   if (todo.completed) {
//     if (completedTasksByUser[todo.userId] === undefined) {
//       completedTasksByUser[todo.userId] = 1;
//     } else {
//       completedTasksByUser[todo.userId]++;
//     }
//   }
// });

// for (const userId in completedTasksByUser) {
//   console.log(
//     `User ${userId}: ${completedTasksByUser[userId]} completed tasks`
//   );
// }
