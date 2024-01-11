#!/usr/bin/node

const argSquare = process.argv;
const number = parseInt(argSquare[2], 10);

if (argSquare[2]) {
  if (number) {
    for (let i = 0; i < number; i++) {
      let square = '';
      for (let j = 0; j < number; j++) {
        square += 'X';
      }
      console.log(square);
    }
  } else {
    console.log('Missing size');
  }
} else {
  console.log('Missing size');
}
