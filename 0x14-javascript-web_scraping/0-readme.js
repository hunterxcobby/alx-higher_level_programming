#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', function (err, data) {
  if (data === undefined) {
    console.error(err);
  } else {
    console.log(data);
  }
});
