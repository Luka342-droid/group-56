// 2) Check if a Number is Positive or Negative

// Ask the user to enter a number.

// Use an if statement to check if it’s positive, negative, or zero, and display a message.
let input = prompt("Enter a number:");
if (input > 0) {
    alert("The number is positive.");
} else if (input < 0) {
    alert("The number is negative.");
} else {
    alert("The number is zero.");
}


// 3) Check User’s Age for Voting Eligibility

// Ask the user to enter their age.

// If the age is 18 or above, show a message saying “You can vote!”

// Otherwise, show “You are not eligible to vote.”
let age = prompt("Enter your age: ")
if (age >= 18) {
    alert("you can vote")
} else {
    alert("you are not eligibleto vote")
}

// 4) Compare Two Numbers

// Ask the user to enter two numbers.

// Use an if...else statement to check which number is larger, or if they are equal, and display a message.
let num1 = prompt("Enter first number: ")
let num2 = prompt("Enter second number: ")
if (num1 > num2) {
    alert("first number is bigger than second")
} else if (num2 > num1) {
    alert("second number is bigger than first")
} else{
    alert("these numbers are equal")
}