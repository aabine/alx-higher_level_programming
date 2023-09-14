#!/bin/usr/node
exports.esrever = function (list) {
  let count = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    count++;
  }
  return count;
};
