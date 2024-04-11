#!/usr/bin/node
// computes and prints a factorial

const n = Number(process.argv[2]);

function fact (n) {
  if (isNaN(n) || n === 0 || n === 1) {
    return 1;
  }
  return (n * fact(n - 1));
}

console.log(fact(n));
