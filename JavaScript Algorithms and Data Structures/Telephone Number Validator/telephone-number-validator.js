function telephoneCheck(str) {
  var result=false
  // create patterns to match and get validated
  var check=str.match(/^(?:[1])?[\s]{0,1}(?:\([\d]{3}\)|[\d]{3})[-\s]{0,1}[\d]{3}[-\s]{0,1}[\d]{4}$/)

  if (check!=null){
    result=true
  }
  console.log(check)
  return result;
}

var num="555-555-5555"
var output = telephoneCheck(num);
console.log("\nIs "+num+ " a phone number? \n" + output)