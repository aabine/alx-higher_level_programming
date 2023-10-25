#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function getRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, function (error, response, body) {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
}

getRequest(url)
  .then(body => {
    const characters = JSON.parse(body).characters;
    return printCharacters(characters, 0);
  })
  .catch(error => {
    console.error(error);
  });

function printCharacters (characters, index) {
  return getRequest(characters[index])
    .then(body => {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        return printCharacters(characters, index + 1);
      }
    })
    .catch(error => {
      console.error(error);
    });
}
