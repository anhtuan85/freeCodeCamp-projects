function checkCashRegister(price, cash, cid) {
  var output = {status: "", change: []};
  var register = cash - price; 
  var value;
  const curr  = [0.01, 0.05, 0.1, 0.25, 1, 5, 10, 20, 100];
  var sum = 0;
  for (let i= 0; i < cid.length ; i++) {
    sum += cid[i][1];
  }
  if (sum < register) {
    output.status = "INSUFFICIENT_FUNDS";
    return output;
  } else if (sum === register) {
    output.status = "CLOSED";
    output.change = cid;
    return output
  } else {
    for (let i = cid.length -1; i > -1; i--) {
      value = 0;
      while (cid[i][1] > 0 && register >= curr[i]) {
        register -= curr[i];
        cid[i][1] -= curr[i];
        value += curr[i];
        register =  Math.round(register * 100) / 100;
      }
      if (value) {
        output.change.push([cid[i][0], value]);
      }
    }
    if (register) {
      console.log(register)
      return {status: "INSUFFICIENT_FUNDS", change: []}
    } else {
      output.status = "OPEN"
      return output;
    }
  }
}

var A = checkCashRegister(3.26, 100, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]])
console.log(A);