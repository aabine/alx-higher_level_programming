#!/usr/bin/node
function add (a, b) {
  a = parseInt(process.argv[2]);
  b = parseInt(process.argv[3]);

  if (process.argv[2] === undefined || isNaN(a)) {
    console.log(NaN);
  } else if (process.argv[3] === undefined || isNaN(b)) {
    console.log(NaN);
  } else {
    console.log(a + b);
  }
}

add();
