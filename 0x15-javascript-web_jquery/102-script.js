$(document).ready(function() {
  $('#btn_translate').click(function() {
    $.getJSON('https://www.fourtonfish.com/hellosalut/hello/' + $('#language_code').val(), function(data) {
      $('#hello').text(data.hello);
    });
  });
});