#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

function fetchCharacterJson (url) {
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

async function fetchCharacterName (urls) {
  for (const url of urls) {
    try {
      const characterJson = JSON.parse(await fetchCharacterJson(url));
      console.log(characterJson.name);
    } catch (err) {
      console.error('Error:', err);
    }
  }
}

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  const movieJsonData = JSON.parse(body);
  fetchCharacterName(movieJsonData.characters);
});
