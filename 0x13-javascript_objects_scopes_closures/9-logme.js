#!/usr/bin/node
let xarg = 0;

exports.logMe = function (item) {
  console.log(xarg + ': ' + item);
  xarg++;
};
