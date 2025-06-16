let Luka = {};

let person = {
    name: "luka",
    age: 14,
    city: "tbilisi"
};

console.log(person.name);

person.country = "georgia";

let user = {
    name: "Luks",
    address: {
        street: "nuh uh",
        city: "tbilisi",
    }
};

person.age = 1000000000000000;


let num1 = 17;
let num2 = 4652;

if (num1 > 10 && num2 > 10) {
    console.log("Both numbers are greater than 10");
}

let age = 14;
let hasLaptop = true;

if ((age > 18 && hasLaptop) || age === 18) {
    console.log("Access granted");
}
