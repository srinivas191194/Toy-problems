var i = 0;
var j = 0;
function countBs(x) {
    var c = 0;
    if(j < x.length){
      if(x[j] === "B")
        c++;
      j++;
       return c + countBs(x);  
      
    }
  return c;
  }
  
  function countChar(newstring, character) {
    let c = 0;
    if(i < newstring.length){
      if(newstring[i] === character)
            c++;
      i++;
       return c + countChar("erAAdgsAh","A");
    
  }
   return c; 
  }
console.log(countChar("erAAdgsAh", "A"));
console.log(countBs("BABA AUTOMICB"));