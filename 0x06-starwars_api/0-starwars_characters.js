#!/usr/bin/node

const request = require('request');
const actorID = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';

request(apiUrl + actorID, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    viewOne(characters);
  }
});

function viewOne (char, i = 0) {
  if (i === char.length) { return; }
  request(char[i], (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const name = JSON.parse(body).name;
      console.log(name);
    }
    viewOne(char, i + 1);
  });
}
