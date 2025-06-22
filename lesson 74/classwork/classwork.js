function addNewElement() {
    let container = document.getElementById("container");
    let button = document.createElement("button");
    let text = document.createTextNode("დაამატე ღილაკი");
    button.appendChild(text);
    container.appendChild(button);
}

addNewElement();

function modifyElements() {
    let container = document.getElementById("container");
    let button = document.getElementById("removeBtn");
    let paragraph = document.getElementById("text");

    container.removeChild(button);

    let italic = document.createElement("i");
    italic.textContent = "ეს არის i თეგი";

    container.replaceChild(italic, paragraph);
}

modifyElements();