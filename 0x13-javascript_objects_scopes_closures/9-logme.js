#!/usr/bin/node
let args = 0;
exports.logme = function (item) {
  console.log(args + ' ' + item);
  args++;
};
