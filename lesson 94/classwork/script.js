let str1 = "Hello";
let str2 = "World";
let result1 = str1.concat(str2);
console.log(result1);

let str3 = "Good";
let str4 = "Morning";
let str5 = "Everyone";
let result2 = str3.concat(str4, str5);
console.log(result2);

let word1 = "JavaScript";
let word2 = "Rocks";
let result3 = word1.concat(" ", word2);
console.log(result3);

let url = "https://www.youtube.com/";
console.log(url.endsWith("/"));

function endsWithS(word) {
  return word.endsWith("s");
}

console.log(endsWithS("cats"));
console.log(endsWithS("dog"));


  
  