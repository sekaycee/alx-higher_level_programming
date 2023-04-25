#!/usr/bin/node
const req = require('request');
const id = process.argv[2];
req.get(`http://swapi.co/api/films/${id}`).on('body', function (body) {
  const data = JSON.parse(body);
  console.log(data.title);
});
