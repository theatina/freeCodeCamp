function checkCashRegister(price, cash, cid) {
  var change = new Object();
  change["status"]=""
  change["change"]=[]
  var change_num=cash-price;

  var currency_dict= new Object();
  currency_dict["PENNY"]=0.01;
  currency_dict["NICKEL"]=0.05;
  currency_dict["DIME"]=0.1;
  currency_dict["QUARTER"]=0.25
  currency_dict["ONE"]=1;
  currency_dict["FIVE"]=5;
  currency_dict["TEN"]=10;
  currency_dict["TWENTY"]=20;
  currency_dict["ONE HUNDRED"]=100;

  var currency_dict_rev = {};
  for(var key in currency_dict){
    currency_dict_rev[currency_dict[key]] = key;
  }
  // console.log(currency_dict_rev[parseInt("1")])

  var total_funds=0;
  for(var i = 0; i < cid.length; i++) {
    total_funds+=cid[i][1]
  }
  // console.log(total_funds, change_num, change)
  if (total_funds < change_num) {
    change["status"]="INSUFFICIENT_FUNDS"
    change["change"]=[]
    console.log(total_funds, change)
    return change
  }

  if (total_funds == change_num) {
    change["status"]="CLOSED"
    change["change"]=cid
    console.log(total_funds, change)
    return change
  }

  const n = [];
  n.push(100,20,10,5,1,0.25,0.1,0.05,0.01);
  
  var change_units = new Array(n.length).fill(0);
  for (let i = change_units.length-1; i >= 0; i--){
    // console.log(8-i)
    // console.log(cid[8-i][1], currency_dict[cid[8-i][0]])
    change_units[i]=Math.floor(cid[8-i][1]/currency_dict[cid[8-i][0]])
    // console.log(change_units[i])
  }
  console.log(change_units) 

  var units_needed = new Array(n.length).fill(0);
  for (let i = 0; i < n.length; i++) {
    if (change_num>=n[i] && change_units[i]>0){
      units_needed[i]=Math.floor(change_num/n[i]);
      console.log(units_needed[i], change_units[i])
      if (units_needed[i]>change_units[i]){
        change["status"]="INSUFFICIENT_FUNDS"
        change["change"]=[]
        console.log(total_funds, change)
        return change
      }
      else {
        change["status"]="OPEN"
        change["change"].push( [ currency_dict_rev[n[i]], units_needed[i]*n[i] ])
      }
      change_num=change_num%n[i]

    }
  }



  // console.log(change_num, change_units) 
  
  console.log(change)
  return change;
}

// checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]);

checkCashRegister(3.26, 100,  [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]])
