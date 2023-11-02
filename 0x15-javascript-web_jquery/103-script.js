$('document').ready(function () {
  const $btnTranslate = $('INPUT#btn_translate');
  const $languageCode = $('INPUT#language_code');
  const $hello = $('DIV#hello');

  $('body').on('click', 'INPUT#btn_translate', translate);
  $('body').on('keydown', 'INPUT#language_code', function (e) {
    if (e.keyCode === 13) {
      translate();
    }
  });
});

function translate() {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  const lang = $languageCode.val();
  $.get(url + $.param({ lang }), function (data) {
    $hello.html(data.hello);
  });
}