#!/usr/bin/node

// import request module
const request = require('request');

// constduct url
const apiurl = 'https://swapi-api.alx-tools.com/api/films/';
const url = process.argv[2] || apiurl;

// make api request
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  try {
    const data = JSON.parse(body);
    const filmdata = data.results;
    const filteredFilm = filmdata.filter(film =>
      film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    );
    console.log(filteredFilm.length);
  } catch (error) {
    console.error('Parse Error:', error);
  }
});
