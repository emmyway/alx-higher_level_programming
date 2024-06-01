$(document).ready(function () {
  const newItem = $('<li>Items</li>');
  $('DIV#add_item').click(function () {
    const newItem = $('<li>Items</li>');
    $('ul.mylist').append(newItem);
  });
});
