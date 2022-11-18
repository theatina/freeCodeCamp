function rot13(str) {
  let decoded=""

  // create dictionary with rot13 shift
  const alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  var rot13_dict={};
  for (let i = 0; i < alphabet.length ; i++){
    var pos=i
    var new_pos=(pos-13) % alphabet.length 
    if (new_pos<0){
      new_pos=new_pos+alphabet.length
    }
    rot13_dict[alphabet[i]]=alphabet[new_pos]

  }

  // console.log(rot13_dict)

  // loop sentence for alphabetic char shifting - keep punctuation
  for (let i = 0; i < str.length ; i++){
    var char=str[i]
    if (char.match(/[a-z]/i)){
      char=rot13_dict[char]
    }
    decoded+=char
  }
  console.log(decoded)
  return decoded;
}

rot13("SERR PBQR PNZC");