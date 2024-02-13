#!/usr/bin/node
const convertedArg = parseInt(process.argv[2]);

if (isNaN(convertedArg) || convertedArg < 1 || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < convertedArg; i++) {
    console.log('X'.repeat(convertedArg));
  }
}
