#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rectChar; // declare var to act as container for printing charcaters
    for (let i = 0; i < this.height; i++) {
      // let the variable be an empty string
      rectChar = '';
      for (let j = 0; j < this.width; j++) {
        // append the X char to the variable in each iteration
        rectChar += 'X';
      }
      console.log(rectChar);
    }
  }

  rotate () {
    // had to refactor and use a temp to first hold the width before swapping
    const tempSwap = this.width;
    this.width = this.height;
    this.height = tempSwap;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
