#!/usr/bin/node
const req = require('request');
const id = process.argv[2];

req(`http://swapi.co/api/films/${id}`, function (err, res, body) {
  if (!err) {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
