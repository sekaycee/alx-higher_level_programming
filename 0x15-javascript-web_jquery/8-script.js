const $ = window.$;
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, textStatus) {
  const res = data.results;
  for (let i = 0; i < res.length; i++) {
    $('UL#list_movies').append('<li>' + res[i].title + '</li>');
  }
});
