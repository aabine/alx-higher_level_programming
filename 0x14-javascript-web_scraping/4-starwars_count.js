#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const results = JSON.parse(body).results;
    const count = results.reduce((count, movie) =>
      movie.characters.some((character) => character.endsWith('/18/')) ? count + 1 : count, 0
    );
    console.log(count);
  } else {
    console.error(error || `${response.statusCode}`);
  }
});
