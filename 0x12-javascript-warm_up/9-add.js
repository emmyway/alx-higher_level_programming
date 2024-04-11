#!/usr/bin/node
// prints adition of two humbers

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

add(a, b);
function add (a, b) {
  console.log(a + b);
}
