$(document).ready(function (){
  // ensure that code is executed only when document is fully loaded
  $('DIV#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});
