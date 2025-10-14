// Helper to show output
function show(id, text) {
    document.getElementById(id).textContent = text;
  }
  
  // 2–6: loops with break/continue
  function printArgs(...args) {
    let out = "";
    for (let arg of args) out += arg + " ";
    show("out1", out);
  }
  
  function countArgs(...args) {
    show("out1", "Count: " + args.length);
  }
  
  function sumArgs(...args) {
    let total = 0;
    for (let arg of args) if (typeof arg === "number") total += arg;
    show("out1", "Sum: " + total);
  }
  
  function stopAtZero(...args) {
    let out = "";
    for (let arg of args) {
      if (arg === 0) break;
      out += arg + " ";
    }
    show("out1", out);
  }
  
  function skipStrings(...args) {
    let out = "";
    for (let arg of args) {
      if (typeof arg === "string") continue;
      out += arg + " ";
    }
    show("out1", out);
  }
  
  // 7–9: Anonymous functions
  const multiply = function(a, b) { return a * b; };
  
  let intervalID;
  function startInterval() {
    intervalID = setInterval(function() {
      console.log("Message every 2 sec");
    }, 2000);
  }
  
  // Button click
  document.getElementById("btnClick").addEventListener("click", function() {
    alert("Button clicked!");
  });
  
  // 10–12: IIFE
  function IIFEHello() {
    (function() { console.log("Hello, world!"); })();
  }
  
  function IFEESquare(num) {
    (function(n){ console.log(n*n); })(num);
  }
  
  function IFEESum(arr) {
    (function(a){
      let sum = 0;
      for (let n of a) sum += n;
      console.log("Sum:", sum);
    })(arr);
  }
  
  // 13–15: Scope examples
  function testLocalVar() {
    function localVar() { let a=10; }
    localVar();
    try { console.log(a); } catch(e){ show("out4", e); }
  }
  
  function nestedFunctions() {
    function outer() {
      let x=5;
      function inner() { x+=10; }
      let before = x;
      inner();
      let after = x;
      return `Before: ${before}, After: ${after}`;
    }
    show("out4", outer());
  }
  
  function varLetConstScope() {
    function scopeTest() {
      if(true){
        var v="var";
        let l="let";
        const c="const";
      }
      let out = "v=" + v;
      try { out += ", l=" + l; } catch(e){ out+=", l=Error"; }
      try { out += ", c=" + c; } catch(e){ out+=", c=Error"; }
      return out;
    }
    show("out4", scopeTest());
  }
  