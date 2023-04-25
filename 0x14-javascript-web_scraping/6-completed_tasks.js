#!/usr/bin/node
const req = require('request');

req.get(process.argv[2]).on('body', function (body) {
  const c_tasks = {};
  const todos = JSON.parse(body);
  for (let i = 0; i < todos.length; i++) {
    if (todos[i].completed === true) {
      if (c_tasks[todos[i].userId] === undefined) {
        c_tasks[todos[i].userId] = 0;
      }
      c_tasks[todos[i].userId]++;
    }
  }
  console.log(c_tasks);
});
