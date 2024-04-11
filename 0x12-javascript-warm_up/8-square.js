#!/usr/bin/node
// prints square

const arg = process.argv[2];
if (isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg; i++) {
    let output = '';
    for (let j = 0; j < arg; j++) {
      output += 'X';
    }
    console.log(output);
  }
}
