#!/usr/bin/node

// import request
const request = require('request');
// validate movie id
const movieId = process.argv[2];
if (!movieId) {
  console.error('provide movie id');
  process.exit(1);
}
// construct the url
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
// make api request
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.log('fail to fetch:', response.statusCode);
    return;
  }
  // handle json parsing"
  try {
    const data = JSON.parse(body);
    console.log(data.title);
  } catch (parseError) {
    console.error('Parse Error:', parseError);
  }
});
