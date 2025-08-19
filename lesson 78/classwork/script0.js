const paragraphs = document.querySelectorAll("p");
const texts = [];
for (let i = 0; i < paragraphs.length; i++) {
  texts.push(paragraphs[i].textContent);
}
console.log(texts);


const container = document.getElementById("container");
for (let i = 1; i <= 5; i++) {
  const p = document.createElement("p");
  p.textContent = "პარაგრაფი " + i;
  container.appendChild(p);
}


