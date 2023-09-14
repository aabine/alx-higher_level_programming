#!/usr/bin/node
const { dict } = require('./101-data');

const userDict = {};
for (const [userId, occurrences] of Object.entries(dict)) {
  if (!userDict[occurrences]) {
    userDict[occurrences] = [];
  }
  userDict[occurrences].push(userId);
}

console.log(userDict);
