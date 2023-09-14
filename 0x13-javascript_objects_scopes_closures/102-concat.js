#!/usr/bin/node
const fs = require('fs');

const destinationFile = process.argv[4];

fs.readFile(process.argv[2], (err, content1) => {
  if (err) throw err;

  fs.readFile(process.argv[3], (err, content2) => {
    if (err) throw err;

    const concatenatedContent = Buffer.concat([content1, content2]);

    fs.writeFile(destinationFile, concatenatedContent, (err) => {
      if (err) throw err;
    });
  });
});
