#!/usr/bin/node
// print the second biggest number from an array

const args = process.argv;

if (args.length <= 3) {
  console.log(0);
} else {
  let arr = args
    .map(Number)
    .slice(2, args.length)
    .sort((a, b) => a - b);
  console.log(arr[arr.length - 2]);
}
