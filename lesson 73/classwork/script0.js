function modifyContent() {
    let container = document.getElementById("myContainer");

    let button = document.getElementById("myButton");
    container.removeChild(button);

    let paragraph = document.getElementById("myParagraph");

    let italicText = document.createElement("i");
    italicText.textContent = "i tag";

    container.replaceChild(italicText, paragraph);
}

modifyContent()