#!/usr/bin/node
const fs = require('fs');

const arg1 = fs.readFileSync(process.argv[2], 'utf8');
const arg2 = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], arg1 + arg2);
