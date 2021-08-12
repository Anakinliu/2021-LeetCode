let line = "101 2 3 4 5";
let lineArr = line.split(' ');
if (lineArr.length > 1) {
    let numStr = lineArr[0];
    let s = 0;
    for (let i = 1; i < lineArr.length; i++) {
        let jz = +lineArr[i];
        jz = jz % 36;
        if (jz < 2) {
            continue;
        }
        console.log(parseInt(numStr, jz));
        s += parseInt(numStr, jz);
    }
    if (s % 2 === 0) {
        console.log(0);
    }
    else {
        console.log(1);
    }
}