const $ = window.$;
window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + lang, function (data, textStatus) {
      $('DIV#hello').text(data.hello);
    });
  });
};
