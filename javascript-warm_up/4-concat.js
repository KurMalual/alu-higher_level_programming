#!/usr/bin/node
function printArguments(...args) {
  for (let i = 0; i < args.length; i++) {
    console.log(args[i] + ' is ');
  }
}

printArguments('Python', 'fun');
printArguments('HBTN');
printArguments();
