#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

function fetchData (url) {
  request(url, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const tasks = JSON.parse(body);
      const completedTasks = tasks.filter(task => task.completed === true);
      const completed = {};

      for (const task of completedTasks) {
        if (completed[task.userId] === undefined) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId]++;
        }
      }

      console.log(completed);
    } else {
      console.error(error || `Error code: ${response.statusCode}`);
    }
  });
}

fetchData(url);
