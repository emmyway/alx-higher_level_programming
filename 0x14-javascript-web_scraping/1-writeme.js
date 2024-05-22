#!/usr/bin/node

// import the fs primises
const fs = require('fs').promises;
// write file in try-cache function
async function writeFileAsync (filePath, content) {
  try {
    await fs.writeFile(filePath, content, 'utf-8');
  } catch (error) {
    console.error(error);
  }
}
// call function with arguments
const filePath = process.argv[2];
const content = process.argv[3];

if (filePath && content) {
  writeFileAsync(filePath, content);
} else {
  console.error('please privide file path and string to wtite');
}
