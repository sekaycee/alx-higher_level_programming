#!/usr/bin/node
const req = require('request');
req.get(process.argv[2], function (err, res, body) {
  if (!err) {
    const data = JSON.parse(body).results;
    console.log(data.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
