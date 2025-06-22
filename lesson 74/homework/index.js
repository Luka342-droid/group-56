document.getElementById("alert").addEventListener("click", function () {
    alert("Button was clicked!");
});

document.getElementById("hoverText").addEventListener("mouseover", function () {
    this.textContent = "You moused over me!";
});

document.getElementById("toggleBox").addEventListener("click", function () {
    this.style.backgroundColor = 
    this.style.backgroundColor === "lightblue" ? "lightgreen" : "lightblue";
});

document.getElementById("textInput").addEventListener("click", function () {
    console.log("Input value:", this.value);
});

document.getElementById("toggleImage").addEventListener("click", function () {
    const img = document.getElementById("image");
    img.style.display = img.style.display === "none" ? "block" : "none";
});