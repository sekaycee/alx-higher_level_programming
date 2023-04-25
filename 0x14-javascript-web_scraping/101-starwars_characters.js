#!/usr/bin/node
const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
req.get(url, function (err, res, body) {
  if (!err) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

function printCharacters (characters, index) {
  req.get(characters[index], function (err, res, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
    }
    if (index++ < characters.length) {
      printCharacters(characters, index++);
    }
  });
}
