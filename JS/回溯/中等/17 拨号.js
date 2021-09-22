/*
 * Complete the 'possibleCombinations' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts INTEGER numbers as parameter.
 */
// 参考力扣的17题
function possibleCombinations(numbers) {
    let m = ['', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ'];
    let ans = [];
    let strN = String(numbers);
    function comb(s, path) {
        // 回溯到头了就返回
        if (s.length === 0) {
            ans.push(path);
            return
        }
        // 获取单个数字后，获得m索引对应的字符
        let c = +s[0];
        if (c === 0 || c === 1) {
            // 1 和 0 对应m中的元素是一个字符
            comb(s.slice(1), path);
        } else {
            for (let k = 0; k < m[c].length; k++) {
                comb(s.slice(1), path + m[c][k]);
            }
        }
    }
    comb(strN, '');
    console.log(ans);
    if (ans[0].length === 0) {
        return 'N/A'
    }
    let res = ans.join(' ');
    return res
}

console.log(possibleCombinations(10));
console.log(possibleCombinations(23));
console.log(possibleCombinations(21));
console.log(possibleCombinations(2103));
console.log(possibleCombinations(102));
console.log(possibleCombinations(234));
console.log(possibleCombinations(1221));
