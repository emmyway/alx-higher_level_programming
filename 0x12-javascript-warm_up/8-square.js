#!/usr/bin/node

const xLen = parseInt(process.argv[2]);

if (isNaN(xLen)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < xLen; i++) {
    let row = '';
    for (let j = 0; j < xLen; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
