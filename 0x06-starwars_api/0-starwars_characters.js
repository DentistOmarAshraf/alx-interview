#!/usr/bin/node
const request = require('request');
const util = require('util');

const requestPromise = util.promisify(request);

const actorId = process.argv[2];
if (!actorId) {
  console.log('Usage: ./0-starwars_characters.js <actorID>');
  process.exit(1);
}
/**
 * async function request for api (starwar)
 * @param {string} actor - actor id passed as argv
 */
async function getCharacter (actor) {
  try {
    const response = await requestPromise({ uri: `https://swapi-api.alx-tools.com/api/films/${actor}` });
    const data = await JSON.parse(response.body);

    for (const url of data.characters) {
      const response = await requestPromise({ uri: url });
      const data = await JSON.parse(response.body);
      console.log(data.name);
    }
  } catch (err) {
    console.error(err);
  }
}

getCharacter(actorId);
