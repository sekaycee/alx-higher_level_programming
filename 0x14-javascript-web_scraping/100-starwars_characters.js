#!/usr/bin/node
const req = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];

req.get(url).on('body', function (body) {
  const resp = JSON.parse(body);
  const characters = resp.characters;
  for (let i = 0; i < characters.length; i++) {
    req.get(characters[i]).on('body', function (body) {
      console.log(JSON.parse(body).name);
    });
  }
});
