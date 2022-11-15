function palindrome(str) {
  str=str.toLowerCase()
  str=str.replace(/[|&;$%@"<>()+-._ ,]/g, "")
  str=str.replace(/  +/g, "")
  console.log(str)
  var pal1=str;
  var pal2=str.split("").reverse().join("");
  if (pal1==pal2) {
    return true;
  }
  return false;
  
}

palindrome("eye");