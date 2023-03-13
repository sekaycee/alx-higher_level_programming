#!/usr/bin/node

if (process.argv.length < 4) {
  console.log('0');
} else {
  const nums = process.argv.slice(2).map(Number);
  console.log(nums.sort((a, b) => a - b)[nums.length - 2]);
}
