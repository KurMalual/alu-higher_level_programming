#!/usr/bin/node

const request = require('require');
const url = 'https://swapi-api.hbtn.io/api/films/';
const ep = process.argv[2];

request(url + ep, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const json = json = JSON.parse(body);
  console.log(json.title);
});
