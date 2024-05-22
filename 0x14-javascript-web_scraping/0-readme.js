#!/usr/bin/node

// importing the fs module with promises API
const fs = require('fs').promises;

// defining an async function
async function readFileAsync(filePath) {
	try {
		//use fs.readFile to read file, await to wait 
		// for the promise to complete reading file
		const data = await fs.readFile(filePath, 'utf-8');
		console.log(data);
	} catch (error) {
		console.error(error)
	}
}

// get the file path from first command line
const filePath = process.argv[2];

if (filePath) {
	readFileAsync(filePath);
} else {
	console.error("pls provide a file path");
}
