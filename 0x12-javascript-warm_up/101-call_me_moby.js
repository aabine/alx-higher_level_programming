#!/usr/bin/node
/**
 * Execute a given function multiple times.
 *
 * @param {number} x - The number of times to execute the function.
 * @param {function} theFunction - The function to be executed.
 */
exports.callMeMoby = function (x, theFunction) {
  Array(x).fill().forEach(theFunction);
};
