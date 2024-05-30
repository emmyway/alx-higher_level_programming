#!/usr/bin/node

// import request module
const request = require('request');
// construct url
const url = process.argv[2];
// make ap jrequest
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  console.log('code:', response.statusCode);
});
