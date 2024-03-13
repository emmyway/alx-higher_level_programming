#!/usr/bin/node

// prints result os sum of two command line int passed
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

function add (a, b) {
  return (a + b);
}

console.log(add(a, b));
