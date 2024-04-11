#!/usr/bin/node
// prints two arguments passed to it, in the following format: “ is ”

const first = process.argv[2];
const second = process.argv[3];

console.log(`${first} is ${second}`);
