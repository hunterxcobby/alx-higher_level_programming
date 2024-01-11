#!/usr/bin/node
const argsNumber = process.argv.length - 2;

if (argsNumber === 0) {
  console.log('No argument');
} else if (argsNumber === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
