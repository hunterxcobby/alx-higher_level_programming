#!/usr/bin/node

const request = require('request');

// Construct the SWAPI URL based on the film ID from the command line arguments
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

// Make a request to the SWAPI URL
request(apiUrl, function (error, response, body) {
  // Check for errors in the request
  if (!error) {
    // Parse the JSON response body to get the list of characters
    const characters = JSON.parse(body).characters;

    // Call the function to print characters, starting from index 0
    printCharacters(characters, 0);
  }
});

// Function to recursively print characters
function printCharacters (characters, index) {
  // Make a request to fetch information about the character at the given index
  request(characters[index], function (error, response, body) {
    // Check for errors in the request
    if (!error) {
      // Print the name of the character
      console.log(JSON.parse(body).name);

      // Check if there are more characters to print
      if (index + 1 < characters.length) {
        // Recursively call the function for the next character
        printCharacters(characters, index + 1);
      }
    }
  });
}
