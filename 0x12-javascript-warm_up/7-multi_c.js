#!/usr/bin/node
const converstedArg = parseInt(process.argv[2]);
if (process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else if (converstedArg < 1 || isNaN(converstedArg)) {
  process.exit(1);
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
}
