#!/usr/bin/node
let num = process.argv[2];
if (!num || isNaN(num)) {
  console.log('Missing size');
} else {
  num = parseInt(num);
  for (let i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
}
