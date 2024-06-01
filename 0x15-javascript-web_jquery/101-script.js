// script performs add remove and clear on a list
$(document).ready(function () {
  // add element to the list
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  // removes item from list
  $('DIV#remove_item').click(function () {
    $('UL.my_list li:last-child').remove();
  });
  // clears the whole list
  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
//
