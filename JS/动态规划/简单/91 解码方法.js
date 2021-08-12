var numDecodings = function(s) {
    let t = [1];  // 空字符串时为1
    // t[i]表示到s的第i-1个字符时总的解码数
    let n = s.length;
    if (s[0] === '0') {
        return 0;
    }
    for (let i=1; i<=n; i++) {
        t[i] = 0;
        if (s[i-1] !== '0') {
            t[i] += t[i-1];
        }
        if (i > 1 && s[i-2] !== '0' && s[i-2] + s[i-1] <= 26) {
            t[i] += t[i-2];
        }  
    }
    console.log(t);
    return t[n];
};

// 优化空间的写法
var numDecodingsNoSpace = function(s) {
    let [a,b,c] = [0,1,0];
    // t[i]表示到s的第i-1个字符时总的解码数
    let n = s.length;
    if (s[0] === '0') {
        return 0;
    }
    for (let i=1; i<=n; i++) {
        c = 0;
        if (s[i-1] !== '0') {
            c += b;
        }
        if (i > 1 && s[i-2] !== '0' && s[i-2] + s[i-1] <= 26) {
            c += a;
        }  
        [a,b] = [b, c];
    }
    // console.log(t);
    return c;
};



// console.log(numDecodings("226"));  // 3
// console.log(numDecodings("21010"));
console.log(numDecodingsNoSpace("2101"));  // 1
// console.log(numDecodings("12"));  // 2
// console.log(numDecodings("0"));  // 0
// console.log(numDecodings("06"));  // 0
// console.log(numDecodings("1123"));  // 5