// Print numbers from 1 to 10 using a for loop.
let num1 = 1
let num2 = 10
for (num1; num1 <=10; num1++) {
    console.log(num1)
}

// Print even numbers from 2 to 20 using a while loop.
let num3 = 2

while (num3 <= 20) {
    console.log(num3)
    num3+=2
}
// Print the numbers from 10 down to 1 using a for loop.
for (num4; num4>=1; num4--) {
    console.log(num4)
}
// Print the first 5 multiples of 3 using a while loop.

// Print each character of a string using a for loop.
let char = "Hello, world!";
for (let i = 0; i < str.length; i++) {
    console.log(str[i]);
}






// Change the text content of a paragraph when a button is clicked.
function changeParagraphText() {
    document.getElementById("div1").textContent = 'hello';
}
// Change the background color of a div when a button is clicked.
function changeBackgroundColor() {
    document.getElementById("div2").style.backgroundColor = "red";
}
// Change the font size of a heading when a button is clicked.
function changeFontSize() {
    document.getElementById("div3").style.fontSize = '15px';
}
// Hide a div by setting its display style to none when a button is clicked.
function hideDiv() {
    document.getElementById("div4").style.display = 'none';
}
// Show an alert with a custom message when a button is clicked.
function alertt() {
    alert("hello world");
}