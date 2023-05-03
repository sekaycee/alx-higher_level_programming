const $ = window.$;
window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    sayHello();
  });
  $('INPUT#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      sayHello();
    }
  });
};

function sayHello () {
  const lang = $('INPUT#language_code').val();
  $.get('https://fourtonfish.com/hellosalut/?lang=' + lang, function (data, textStatus) {
    $('DIV#hello').text(data.hello);
  });
}
