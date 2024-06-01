$(document).ready(function () {
  $('DIV#add_item').click(function () {
    const newItem = $('<li>Items</li>');
    $('ul.mylist').append(newItem);
  });
});
