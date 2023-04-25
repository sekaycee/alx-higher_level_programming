#!/usr/bin/node
const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
req.get(url, function (err, res, body) {
  if (!err) {
    const characters = JSON.parse(body).characters;
    for (let i = 0; i < characters.length; i++) {
      req.get(characters[i], function (err, res, body) {
        if (!err) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
