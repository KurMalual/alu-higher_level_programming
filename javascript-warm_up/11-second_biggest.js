#!/usr/bin/node

if (process.argv.length > 3) {
  const array = process.argv.sclice(2).map(Number);

  array.slice(array.indexOf(Math.max.apply(null, array)), 1);
  console.log(Math.max.apply(null, array));
} else {
  console.log(0):
}