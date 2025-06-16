// 2) 

// Determine if a number is even or odd.

// Take a number as input.

// Use a conditional statement to check if the number is even or odd.

// Display the result.
let number = prompt("Enter a number:");

number = Number(number);

if (number % 2 === 0) {
    alert("The number is even.");
} else {
    alert("The number is odd.");
}

// 3)

// Assign a grade based on a score.

// Take a score as input.

// Use conditional statements to assign a grade based on the following:

// 90 and above: Grade A

// 80–89: Grade B

// 70–79: Grade C

// 60–69: Grade D

// Below 60: Fail

// Display the grade.
let score = Number(prompt("Enter score: "))
if (score >= 90) {
    alert("Grade A")
} else if (score >= 80) {
    alert("Grade B")
} else if (score >= 70) {
    alert("Grade C")
} else if (score >= 60) {
    alert("Grade D")
} else {
    alert("You failed nigga")
}

// 4)

// Determine the largest among three numbers.

// Take three numbers as inputs.

// Use conditional statements to find and display the largest number.

// If numbers are equal, mention it.
num1 = Number(prompt("Enter first number: "))
num2 = Number(prompt("Enter second number: "))
num3 = Number(prompt("Enter third number: "))

if (num1 > num2 && num1 > num3) {
    alert(num1 + " is the biggest number")
} else if (num2 > num1 && num2 > num3) {
    alert(num2 + " is the biggest number")
} else{
    alert(num3 + " is the biggest number")
}

// 5)

// Check if a character is a vowel or a consonant.

// Take a single character as input.

// Use conditional statements to check if it’s a vowel (a, e, i, o, u) or a consonant.

// Display the result.
let char = prompt("Enter characther: ")
if ( char === 'a' || char === 'e' || char === 'i' || char === 'o' || char === 'u' ) {
    alert(char + " is vowel")
} else{
    alert(char + " is consostant")
}

// 6)

// Check if a number is divisible by 3 and 5.

// Take a number as input.

// Use conditional statements to check if it’s divisible by both 3 and 5.

// Display appropriate messages:

// Divisible by both

// Divisible by 3 only

// Divisible by 5 only

// Not divisible by either
num = Number(prompt("Enter number: "))
if (num % 3 == 0 && num % 5 == 0) {
    alert("divisible by both: 3 and 5")
} else if (num % 3 == 0 && num % 5 != 0) {
    alert("divisible by 3 only")
} else if (num % 3 != 0 && num % 5 == 0) {
    alert("divisible by 5 only")
} else {
    alert("not divisible by either")
}

// 7)

// Check if a person is a child, teenager, adult, or senior based on age.

// Take age as input.

// Use conditional statements to classify:

// 0–12: Child

// 13–19: Teenager

// 20–59: Adult

// 60 and above: Senior

// Display the category.
age = Number(prompt("Enter your age: "))
if (age <= 12) {
    alert("Child")
} else if (age <= 19) {
    alert("Teenager")
} else if (age <= 59) {
    alert("Adult")
} else{
    alert("Senior")
}

// 8)

// Print numbers from 1 to 5.

// Use a while loop to print numbers from 1 to 5, each on a new line.
let num5 = 0;

while (num5 < 5) {
    console.log(num5);
    num5 += 1
}
// 9)

// Print even numbers from 2 to 10.

// Use a while loop to print even numbers starting from 2 up to 10.

let num6 = 2
while(num6 < 10) {
    console.log(num6);
    num6 += 2
}

// 10)

// Print numbers from 10 down to 1.

// Use a while loop to print numbers in reverse from 10 down to 1.

let num7 = 10
while (num7 > 1) {
    console.log(num7);
    num7 -= 1
}