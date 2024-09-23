#!/usr/bin/node
/**
 * Star War API
 */

const request = require('request');

if (process.argv.length < 3) { process.exit(1); }

/* actorId will be passed as argment */
const actorId = process.argv[2];
const apiFullPath = `https://swapi-api.alx-tools.com/api/films/${actorId}`;

request.get(apiFullPath, (error, respons, body) => {
  if (!error && respons.statusCode === 200) {
    const data = JSON.parse(body).characters;
    viewName(data);
  }
});

/**
 * viewName - Recursive function due to
 * inabillity to async request function
 * @param {Array} actor
 * @param {number} i
 * @param {Array} listOfActor
 */
function viewName (actor, i = 0, listOfActor = []) {
  if (i === actor.length) {
    for (const act of listOfActor) { console.log(act); }
    return;
  }
  request.get(actor[i], (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const name = JSON.parse(body).name;
      listOfActor.push(name);
      viewName(actor, i = i + 1, listOfActor);
    }
  });
}
