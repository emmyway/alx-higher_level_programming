#!/usr/bin/node
const list = require('./100-data').list;
const newlist = list.map((val, index) => val * index);
console.log(list);
console.log(newlist);
