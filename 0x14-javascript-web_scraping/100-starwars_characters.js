#!/usr/bin/node

// Require the 'request' module
const request = require('request');

// Get movieID from command line args
const movieId = process.argv[2];
// Get the URl for SWAPI film API
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make request to the SWAPI film API
request(apiUrl, (error, response, body) => {
  if (error) {
    // check for errors in the request
    console.error(error);
  } else if (response.statusCode === 200) {
    // if statusCode is 200 (OK), proceed

    const movieData = JSON.parse(body); // Parse the JSON body response

    // Iterate over each character in the movie
    for (const characterURL of movieData.characters) {
      // Make another request to fetch info on each characters
      request(characterURL, (error, response, charBody) => {
        // Check for errors in the request for character details
        if (error) {
          console.log(error);
        } else if (response.statusCode === 200) {
          console.log(JSON.parse(charBody).name);
        }
      });
    }
  } else {
    // if response statusCode is not 200, output error message
    console.log('Error code: ' + response.statusCode);
  }
});
