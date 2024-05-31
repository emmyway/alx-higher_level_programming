// script retrieves dta and shows title f films from it
$(document).ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.getJSON(url, function (data) {
    const filmTitle = data.results;
    filmTitle.forEach(function (film) {
      const title = film.title;
      $('UL#list_movies').append(`<li>${title}</li>`);
    });
  });
});
