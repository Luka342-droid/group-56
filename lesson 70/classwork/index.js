// საკლასო დავალება:

// შექმენით ფუნქცია სახელად userLoop. ამ ფუნქციაში მომხმარებელს შემოატანინეთ ორი რიცხვი და შეინახეთ ისინი ცვლადებში, number მონაცემთა ტიპში.

// თქვენი დავალებაა, რომ პირველი რიცხვიდან მეორე რიცხვამდე ყველა რიცხვი დაბეჭდოთ კონსოლში. გამოიყენეთ ნებისმიერი ციკლი.

// ეს ფუნქცია გაუშვით მაშინ, როდესაც ვებსაიტი ჩაიტვირთება

function userLoop(num1,num2) {
    num1 = Number(prompt("Enter first number: "))
    num2 = Number(prompt("Enter second number: "))
    for (let i = first; i <= second; i+1) {
        console.log(i);
    }
}

function changeElements() {
    let input = document.getElementById('id1');
    let button = document.getElementById('id2');
    let header = document.getElementById('id3');

    console.log("Input value:", input.value);

    button.style.backgroundColor = 'black';
    button.style.color = 'white';

    header.style.textAlign = 'center';

    document.body.style.backgroundColor = 'green';
}