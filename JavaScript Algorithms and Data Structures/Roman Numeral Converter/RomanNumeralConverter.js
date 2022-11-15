function convertToRoman(num) {
  let roman_str=""
  // var n;
  const n = [];
  n.push(1000,900,500,400,100,90,50,40,10,9,5,4,1);
  const rom = [];
  rom.push('M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I');

  for (let i = 0; i < n.length; i++) {
    if (num>=n[i]){
      roman_str+=rom[i].repeat(num/n[i]);
      num=num%n[i];
    }
  } 

  return roman_str;
}

convertToRoman(36);