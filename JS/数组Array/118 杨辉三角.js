/**
 * @param {number} numRows
 * @return {number[][]}
 */
 var generate = function(numRows) {
    let res = [];
    for (let i=0; i < numRows; i++) {
        let line = [1];
        for (let j=1; j < i; j++) {
            line.push(res[i-1][j] + res[i-1][j-1]);
        }
        if (i) line.push(1);
        res.push(line);
    }
    return res;
};

// 错位相加,@陆诚
var generate2 = function(numRows) {
    let res = [[1]];
    for (let i=1; i < numRows; i++) {
        let a = [1, ...res[i-1]];
        let len = i + 1;
        for (let j=1; j < len-1; j++) {
            a[j] = a[j] + res[i-1][j+1]
        }
        a.push[1];
        res.push(a);
    }
    return res;
};

