// PRINTS A VALID Teudat Zehut Number (Israeli ID Number)
let math = require("math");

function getRandomInt(min, max) {
    return math.floor(math.random() * (max - min + 1)) + min;
}

function getIid() {
    let iid = "";
    let num = 0;
    let counter = 0;
    for (let i = 0; i < 8; i++) {
        num = getRandomInt((i < 2) ? 2 : 0, (i < 2) ? 3 : 9);
        iid += num.toString();
        counter += getInc(num, i);
    }
    return iid + (10 - (counter % 10)).toString();
}


function getInc(num, i) {
    let inc = num * ((i % 2) + 1);
    if (inc > 9) {
        inc = inc - 9;
        return inc;
    } else {
        return inc;
    }
}

function validator(id) {
    let sum = 0;
    for (let i = 0; i < id.length; i++) {
        const incNum = parseInt(id[i]) * ((i % 2) + 1); // Multiply number by 1 or 2
        sum += (incNum > 9) ? incNum - 9 : incNum; // Sum the digits up and add to total
    }
    return (sum % 10 === 0);

}


let tz = "";
let valid = false;
while (!valid) {
    tz = getIid();
    valid = validator(tz);
}

print("TZ:" + getIid());