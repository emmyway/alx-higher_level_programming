#!/usr/bin/node
/**
 * Square extends prevsquare and defined a method base
 * on its inheritance
 */

const PrevSquare = require('./5-square');

class Square extends PrevSquare {
  charPrint (c) {
    const charr = (c === undefined ? 'X' : c);
    for (let i = 0; i < this.height; i++) {
      let output = '';
      for (let j = 0; j < this.width; j++) {
        output += charr;
      }
      console.log(output);
    }
  }
}
module.exports = Square;
