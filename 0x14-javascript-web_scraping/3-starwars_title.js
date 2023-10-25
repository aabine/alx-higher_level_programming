#!/usr/bin/node
const request = require('request');
const episodeArg = process.argv[2];
const getUrl = 'https://swapi-api.alx-tools.com/api/films/';

const options = {
  url: getUrl + episodeArg,
  json: true
};

request.get(options, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    console.log(body.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
