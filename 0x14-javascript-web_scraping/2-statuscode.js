#!/usr/bin/node
const req = require('request');
req.get(process.argv[2]).on('response', function (res) {
  console.log(`code: ${res.statusCode}`);
});
