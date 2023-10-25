#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

async function getCharacterNames(urls) {
  const responses = await Promise.all(urls.map(url => req.get(url)));
  const characterNames = responses.map(response => {
    const data = JSON.parse(response.body);
    return data.name;
  });
  return characterNames;
}

req.get(url + id, function (error, res, body) {
  if (error) {
    console.log(error);
    return;
  }
  const data = JSON.parse(body);
  const characterUrls = data.characters;
  getCharacterNames(characterUrls).then(characterNames => {
    characterNames.forEach(name => console.log(name));
  });
});