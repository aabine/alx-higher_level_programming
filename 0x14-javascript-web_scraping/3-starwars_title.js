#!/usr/bin/node
const request = require('request');
const episode_arg = process.argv[2];
const get_url = 'https://swapi-api.alx-tools.com/api/films/';

const options = {
  url: get_url + episode_arg,
  json: true
};

request.get(options, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode == 200) {
    console.log(body.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
