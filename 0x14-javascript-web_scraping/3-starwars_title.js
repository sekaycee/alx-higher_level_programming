#!/usr/bin/node
const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
req.get(url, function (err, res, body) {
  if (!err) {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
