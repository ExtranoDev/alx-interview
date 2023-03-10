#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/flims/${process.argv[2]}`;

request.get(url, async (err, res, body) => {
  if (err) console.log(err);
  for (const charUrl of JSON.parse(body).characters) {
    await new Promise((resolve, reject) => {
      request.get(charUrl, (err, res, body) => {
        if (err) reject(err);
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
