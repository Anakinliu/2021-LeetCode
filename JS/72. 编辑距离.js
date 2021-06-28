/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */

var minDistance = function (word1, word2) {

    let word1Arr = word1.split("");
    let word2Arr = word2.split("");

    // word1的长度为列数
    // word2的长度为行数
    let dpArr = [];
    for (let i = 0; i <= word1Arr.length; i++) {
        dpArr.push(new Array(word2Arr.length + 1).fill(-1));
    }
    // console.log(dpArr);
    const solu = function (w1, w2, l1, l2) {
        if (l1 === 0) {
            return l2
        }
        if (l2 === 0) {
            return l1
        }
        
        if (dpArr[l1][l2] >= 0) {
            return dpArr[l1][l2]
        }
        let ans;
        if (w1[l1 - 1] === w2[l2 - 1]) {
            ans = solu(w1, w2, l1 - 1, l2 - 1);
        }
        else {
            ans = Math.min(solu(w1, w2, l1 - 1, l2 - 1),
                solu(w1, w2, l1 - 1, l2),
                solu(w1, w2, l1, l2 - 1)) + 1;
        }
        return dpArr[l1][l2] = ans;
    }
    // console.log(dpArr);
    return solu(word1Arr, word2Arr, word1Arr.length , word2Arr.length)

};

console.log(minDistance("cd", "acc"));