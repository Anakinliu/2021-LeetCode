function jumpFloorII(number)
{
    // write code here
    let t = [0,1,2];
    for (let i=3; i <= number; i++) {
        let s = 0;
        for (let j=1; j < i; j++) {
            s += t[j];
        }
        t[i] = s + 1;
    }
    console.log(t[9]);
    return t[number];
}

console.log(jumpFloorII(3));