// script fetches and prints how to say hello depending on lang

// on document ready
$(document).ready(function () {
  // function to fetch and display hello greeting
  function fetchHello () {
    const helloLang = $('INPUT#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${helloLang}`;
    $.getJSON(url, function (data) {
      $('DIV#hello').text(data.hello);
    });
  }
  // on button click
  $('INPUT#btn_translate').click(function () {
    fetchHello();
  });
  // on enter key
  $('INPUT#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      fetchHello();
    }
  });
});
