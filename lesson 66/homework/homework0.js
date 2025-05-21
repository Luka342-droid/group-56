// Check if Two Numbers Are Equal
let num1 = 5;
let num2 = 5;
console.log("Are the numbers equal?", num1 === num2);  // true

// Check if a Number is Greater Than Another Number
let num3 = 10;
let num4 = 7;
console.log("Is the first number greater?", num3 > num4);  // true

// Check if a Number is Less Than or Equal to Another Number
let num5 = 3;
let num6 = 3;
console.log("Is the first number less than or equal?", num5 <= num6);  // true

// Check if Two Numbers Are Not Equal
let num7 = 8;
let num8 = 6;
console.log("Are the numbers not equal?", num7 !== num8);  // true

// Check if a Number is Greater Than or Equal to 100
let num9 = 105;
console.log("Is the number at least 100?", num9 >= 100);  // true

// 7. Show a confirm box asking a question. The result (true or false) is logged to the console.
const result = confirm("Do you agree to the terms?");
console.log(result);

// 8. Show a confirm box when a button is clicked. Store the result in a variable.
document.getElementById('confirmButton').addEventListener('click', function() {
    const userChoice = confirm("Are you sure you want to proceed?");
    // You can use userChoice variable for further processing
});

// 9. Display a confirm box on page load. Immediately show the result in an alert.
window.onload = function() {
    const pageLoadConfirm = confirm("Welcome! Do you want to continue?");
    alert("You selected: " + pageLoadConfirm);
};

// 10. On form submit, log the value of the input with name="username" to the console.
document.querySelector('form').addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent actual form submission for demonstration
    const username = document.querySelector('input[name="username"]').value;
    console.log(username);
});

// 11. On a button click, clear the value of the input with name="email".
document.getElementById('clearEmailButton').addEventListener('click', function() {
    document.querySelector('input[name="email"]').value = '';
});

// 12. On a button click, alert the value of the input with name="phone".
document.getElementById('showPhoneButton').addEventListener('click', function() {
    const phone = document.querySelector('input[name="phone"]').value;
    alert(phone);
});