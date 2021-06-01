/** TAG：字符串
 * @param {number} n
 * @return {string}
 * 
 n      res
 1.     1
 2.     11
 3.     21
 4.     1211
 5.     111221 
 6.     312211
 7.     13112221
 8.     1113213211
 9.     31131211131221
10.     13211311123113112211
 */
 var countAndSay = function(n) {
     // 基本情况
    if (n == 1) {
        return '1';
    }
    if (n == 2) {
        return '11';
    }

    let mm = '11';
    let res = '';
    for (let i = 3; i <= n; i++) {
        let pre = mm[0];
        let count = 1;
        for (let j=1; j < mm.length; j++) {
            if (pre === mm[j]) {
                count += 1;
            } else {
                res = res + count + pre;
                count = 1;
                pre = mm[j];
            }
        }
        res = res + count + pre;
        mm = res
        res = ''
    }
    return mm;
};

// let m = 112334;
// let n = m + '';
// console.log(typeof n);
// console.log(n[5]);
for (let i=3; i <= 30; i++) {
    console.log(countAndSay(i));
}
