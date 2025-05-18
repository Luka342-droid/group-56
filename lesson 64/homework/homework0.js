// --------- Tasks 2–5 ---------

function askHobby() {
    const hobby = prompt("What is your favorite hobby?");
    alert("Your favorite hobby is: " + hobby);
  }
  
  function askFullName() {
    const firstName = prompt("Enter your first name:");
    const lastName = prompt("Enter your last name:");
    const fullName = `${firstName} ${lastName}`;
    alert("Your full name is: " + fullName);
  }
  
  function updateMessage() {
    const message = prompt("Enter a message to show on the page:");
    document.getElementById("messagePara").textContent = message;
  }
  
  function askEmoji() {
    const emoji = prompt("What is your favorite emoji?");
    alert(`Thank you! Your favorite emoji is: ${emoji}`);
  }
  
  function updatePageTitle() {
    const word = prompt("Enter a word to set as the page title:");
    document.title = word;
  }
  
  // Call the prompt functions
  askHobby();
  askFullName();
  updateMessage();
  askEmoji();
  updatePageTitle();
  
  // --------- Tasks 6–8 ---------
  
  // Task 6: Show alert with text input
  document.getElementById("textForm").addEventListener("submit", function(e) {
    e.preventDefault();
    const value = document.getElementById("textInput").value;
    alert("You typed: " + value);
  });
  
  // Task 7: Change background color
  document.getElementById("colorForm").addEventListener("submit", function(e) {
    e.preventDefault();
    const color = document.getElementById("colorInput").value;
    document.body.style.backgroundColor = color;
  });
  
  // Task 8: Combine names and show in <h1>
  document.getElementById("nameForm").addEventListener("submit", function(e) {
    e.preventDefault();
    const first = document.getElementById("firstNameInput").value;
    const last = document.getElementById("lastNameInput").value;
    document.getElementById("fullNameDisplay").textContent = `${first} ${last}`;
  });
  