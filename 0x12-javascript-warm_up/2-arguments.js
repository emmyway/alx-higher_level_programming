#!/usr/bin/node

// cal. argument length
const myArrLen = process.argv.length;
// compare and infer
if (myArrLen === 2) {
  console.log('No argument');
} else if (myArrLen === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
