$(document).ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  // make request
  $.getJSON(url, function (data) {
    const characterName = data.name;

    // display the name in the DIV element
    $('DIV#character').text(characterName);
  });
});
