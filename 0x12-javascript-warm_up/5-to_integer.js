#!/usr/bin/node

const myArg = parseInt(process.argv[2]);

if (isNaN(myArg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myArg);
}
