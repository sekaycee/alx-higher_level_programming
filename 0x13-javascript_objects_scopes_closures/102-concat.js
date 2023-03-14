#!/usr/bin/node
const fs = require('fs');
const fFile = fs.readFileSync(process.argv[2]).toString();
const sFile = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], fFile + sFile);
