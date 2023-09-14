#!/usr/bin/node
const datas = require('./100-data').list;
console.log(datas);
const narray = datas.map((item, index) => item * index);
console.log(narray);
