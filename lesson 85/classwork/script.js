function printEvenNumbers(a, b, c, d, e, f, g, h, i, j) {
    const args = [a, b, c, d, e, f, g, h, i, j];
    for (const num of args) {
      if (num % 2 === 0) {
        console.log(num);
      }
    }
  }
  
  const anonFunc = function() {
    console.log("anonimuri");
  }; // ეს არის ანონიმური ფუნქცია
  
  function notAnonFunc() {
    console.log("ara-anonimuri");
  } // ეს არ არის ანონიმური ფუნქცია
  
  console.log(
    (function() {
      return "hello";
    })()
  );

  let globalVar = "global";
console.log(globalVar);

function myFunc() {
  let functionVar = "function";
  console.log(functionVar);
}
myFunc();

{
  let blockVar = "block";
  console.log(blockVar);
}