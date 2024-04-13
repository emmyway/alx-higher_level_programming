#!/usr/bin/node
// prints a Rectangle class

class Rectangle {
  constructor (w, h) {
    if (w > 0 && Number.isInteger(w) && h > 0 && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    }
  }

  // print the rectangle
  print () {
    for (let i = 0; i < this.height; i++) {
      let output = '';
      for (let j = 0; j < this.width; j++) {
        output += 'X';
      }
      console.log(output);
    }
  }

  // rotates the rectangle: exchange width with height
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // doublesnthe size of rectangle
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
