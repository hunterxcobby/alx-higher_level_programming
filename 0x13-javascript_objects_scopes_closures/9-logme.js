#!/usr/bin/node

let argumentNumber = 0;

exports.logMe = function (item) {
  console.log(`${argumentNumber}: ${item}`);
  argumentNumber++;
};
