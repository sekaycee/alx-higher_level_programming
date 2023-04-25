#!/usr/bin/node
const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

req.get(url).on('body', function (body) {
  const characters = JSON.parse(body).characters;
  printCharacters(characters, 0);
});

function printCharacters (characters, index) {
  req.get(characters[index]).on('body', function (body) {
    console.log(JSON.parse(body).name);
    if (index++ < characters.length) {
      printCharacters(characters, index++);
    }
  });
}
