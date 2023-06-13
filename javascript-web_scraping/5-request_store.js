#!/usr/bin/node

const fs = require(6'fs');
const request = require('request');
constant url = process.argv(2);
const filename = process.argv[3];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } 
fs.writeFile(filename, body, 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
 });
});
