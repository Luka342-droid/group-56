let p = document.createElement("p");
p.textContent = "This is a new paragraph.";
document.body.appendChild(p);

let h1 = document.createElement("h1");
h1.textContent = "This is a heading";
let container = document.getElementById("container");
container.appendChild(h1);

let img = document.createElement("img");
img.src = "https://via.placeholder.com/150";
img.alt = "Placeholder image";
document.body.appendChild(img);

let button = document.createElement("button");
button.textContent = "Click me";
document.body.appendChild(button);