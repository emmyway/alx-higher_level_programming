// script fetches data from api and display
// greeting according to user input
$(document).ready(function () {
  // on click
  $('INPUT#btn_translate').click(function () {
    const userLang = $('INPUT#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${userLang}`;
    // fetch data
    $.getJSON(url, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
