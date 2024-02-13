#!/usr/bin/node
function findSecondBiggestInteger (args) {
  const numbers = args.map(Number);
  const uniqueNumbers = [...new Set(numbers)];

  if (uniqueNumbers.length < 2) {
    return 0;
  }

  const sortedNumbers = uniqueNumbers.sort((a, b) => b - a);
  return sortedNumbers[1];
}

const input = process.argv.slice(2);
const result = findSecondBiggestInteger(input);
console.log(result);
