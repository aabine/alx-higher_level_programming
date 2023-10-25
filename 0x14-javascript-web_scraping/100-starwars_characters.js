#!/usr/bin/node

const request = require('request');

function getRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
}

const id = process.argv[2];
const filmUrl = `https://swapi-api.hbtn.io/api/films/${id}`;

getRequest(filmUrl)
  .then(filmData => {
    const film = JSON.parse(filmData);
    const characterPromises = film.characters.map(characterUrl => getRequest(characterUrl));

    return Promise.all(characterPromises);
  })
  .then(characterDataArray => {
    const characters = characterDataArray.map(characterData => JSON.parse(characterData));
    characters.forEach(character => console.log(character.name));
  })
  .catch(error => {
    console.log(error);
  });
