const fs = require('fs');
const path = require('path');

const input = fs.readFileSync(path.resolve(__dirname, 'day1.txt'), 'utf8');
const lines = input.split('\n');
const numbers = lines.map(line => line.split('  ').map(Number));
const leftColumn = numbers.map(pair => pair[0]).sort((a, b) => a - b);
const rightColumn = numbers.map(pair => pair[1]).sort((a, b) => a - b);
console.log(leftColumn);
let totalDistance = 0;

for (let i = 0; i < leftColumn.length; i++) {
  let distance = Math.abs(leftColumn[i] - rightColumn[i]);
  totalDistance += distance;
}

console.log(totalDistance);
let similarityScore = 0;

for (let i = 0; i < leftColumn.length; i++) {
  const count = rightColumn.filter(num => num === leftColumn[i]).length;
  let value = leftColumn[i] * count;
  similarityScore += value;
}

console.log(similarityScore);