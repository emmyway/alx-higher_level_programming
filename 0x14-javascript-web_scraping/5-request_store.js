#!/usr/bin/node

// import request and fs
const fs = require('fs');
const request = require('request');

// accept and validate input url and path
const urlContent = process.argv[2];
const filepathDest = process.argv[3];

if (!urlContent || !filepathDest) {
  console.log('Usage: <url_of_content> <filepath>');
  process.exit(1);
}

// request for content
request(urlContent, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // write file and store
  fs.writeFile(filepathDest, body, 'utf-8', (err) => {
    if (err) {
      console.error('write error:', err);
    }
  });
});
