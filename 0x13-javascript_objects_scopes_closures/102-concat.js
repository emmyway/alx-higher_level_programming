#!/usr/bin/node

// import file system
const fs = require('fs');

// validate input
if (process.argv.length !== 5) {
  console.log('Usage: node ./102-concate.js <fileA_path> <fileB_path> <fileC_path>');
  process.exit(1);
}

// extract command line argument
const [,, fileA, fileB, destFile] = process.argv;

// read source1 file
fs.readFile(fileA, 'utf8', (err, data1) => {
  if (err) {
    console.error(`error reading ${fileA}: ${err}`);
    process.exit(1);
  }

  // read source2 file
  fs.readFile(fileB, 'utf8', (err, data2) => {
    if (err) {
      console.log(`error reading ${fileB}: ${err}`);
      process.exit(1);
    }

    // concatenate the two files' data
    const concatData = data1 + data2;

    // write concatData into destFile
    fs.writeFile(destFile, concatData, 'utf8', (err) => {
      if (err) {
        console.log(`error writing to ${destFile}: ${err}`);
        process.exit(1);
      }
    });
  });
});
