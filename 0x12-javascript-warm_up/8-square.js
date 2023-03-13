#!/usr/bin/node
const num = parseInt(process.argv[2]);
if (!num) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      console.log('X');
    }
  }
}
