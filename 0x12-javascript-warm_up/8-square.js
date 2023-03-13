#!/usr/bin/node
const num = parseInt(process.argv[2]);
if (!num) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let tmp = '';
    for (let j = 0; j < num; j++) {
      tmp += 'X';
      if (j === num - 1) {
        console.log(tmp);
      }
    }
  }
}
