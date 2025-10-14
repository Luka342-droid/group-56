let value1 = prompt("Enter the first value:");
let value2 = prompt("Enter the second value:");

if (isNaN(value1)) {
  console.log("Value 1: Is not a number");
} else {
  console.log("Value 1: Is number");
}

if (isNaN(value2)) {
  console.log("Value 2: Is not a number");
} else {
  console.log("Value 2: Is number");
}


let num1 = prompt("Enter the first decimal number:");
let num2 = prompt("Enter the second decimal number:");

let sumInt = parseInt(num1) + parseInt(num2);
let sumFloat = parseFloat(num1) + parseFloat(num2);

console.log("Sum with parseInt:", sumInt);
console.log("Sum with parseFloat:", sumFloat);
console.log("Are sums strictly equal?", sumInt === sumFloat);

let expression = prompt("Enter a math expression:");

let result = eval(expression);
let intResult = parseInt(result);
let floatResult = parseFloat(result);

console.log("Original expression:", expression);
console.log("Evaluated result:", result);
console.log("Integer conversion:", intResult);
console.log("Float conversion:", floatResult);

