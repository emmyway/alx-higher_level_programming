#!/usr/bin/node

let myArg = process.argv[2];
if (myArg)
	console.log(myArg);
else
	console.log('No argument');
