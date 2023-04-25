#!/usr/bin/node
const req = require('request');
req.get(process.argv[2], function (err, res, body) {
  if (!err) {
    const cTasks = {};
    const todos = JSON.parse(body);
    for (let i = 0; i < todos.length; i++) {
      if (todos[i].completed === true) {
        if (cTasks[todos[i].userId] === undefined) {
          cTasks[todos[i].userId] = 0;
        }
        cTasks[todos[i].userId]++;
      }
    }
    console.log(cTasks);
  }
});
