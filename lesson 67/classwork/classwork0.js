let person = {
    name: "Luka",
    surname: "amashukeli",
    academy: "GOA",
    city: "tbilisi",
    role: "student",
    favColor: "red",
    printFullName: function() {
        console.log(this.name + " " + this.surname);
    },
    printFavColor: function() {
        console.log(this.favColor);
    }
};

console.log(person);

console.log(person.city);

person.printFullName();
person.printFavColor();

person.favColor = "green";
console.log(person.favColor);

function userOperations() {
    let confirm1 = confirm("do u want to move up to n2?");
    let confirm2 = confirm("are you sure in your answer?");

    console.log("confirm1 AND confirm2 =", confirm1 && confirm2);
    console.log("confirm1 OR confirm2 =", confirm1 || confirm2);
    }

document.addEventListener("DOMContentLoaded", userOperations);