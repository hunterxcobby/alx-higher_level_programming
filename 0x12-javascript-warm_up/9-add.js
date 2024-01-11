#!/usr/bin/node

const firstArg = parseInt(process.argv[2]);
const secondArg = parseInt(process.argv[3]);

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return NaN;
  }
  return a + b;
}
console.log(add(firstArg, secondArg));
