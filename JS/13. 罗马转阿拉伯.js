var romanToInt = function (s) {
    let d = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    let n = s.length;
    let idx = 0;
    let nxt = 1;
    let res = 0;
    while (idx < n) {
        if (nxt < n && d[s[idx]] < d[s[nxt]]) {
            res -= d[s[idx]];
        } else {
            // 虽然nxt越界,但是这里不用nxt
            res += d[s[idx]];
        }
        idx += 1;
        nxt += 1;
    }
    return res;
    console.log(res);
};
romanToInt("MCMXCIV")