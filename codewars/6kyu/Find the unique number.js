/** 题目描述
 * 给定一个数字数组，包含一个与众不同的数字，找出它
 * 
 * findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55

数组会包含非常多元素，包含浮点数，Infinity，NaN等
 */

/**
 * 我的提交，
 */
function findUniq(arr) {
    let len = arr.length;
    let leftP = 0;
    let mostE, oneE = 0;
    // 主体分两种情况
    if (arr[leftP] === arr[len - 1]) {
        // 情况一，最左最右相等，则那个数在里面，挨个遍历
        mostE = arr[leftP];
        while (leftP < len) {
            leftP++;
            if (arr[leftP] !== mostE) {
                oneE = arr[leftP];
                break;
            }
        }
    } else {
        // 情况二，不相等，必有一个是答案，直接对比第二个元素
        if (arr[leftP + 1] === arr[leftP]) {
            oneE = arr[len - 1];
        } else {
            oneE = arr[leftP];
        }
    }
    return oneE;
}

/**
 * 以下是答案区分享的
 */

function findUniq2(arr) {
    // 因为只有一个，所以其第一次出现的索引必定等于最后一次出现的索引
    return arr.find(n => arr.indexOf(n) === arr.lastIndexOf(n));
}

/**
 * 这个更暴力，排序
 */
function findUniq3(arr) {
    arr.sort((a,b)=>a-b);
    return arr[0]==arr[1]?arr.pop():arr[0]
}
  
/**
 * 这个有意思
 */
function findUniq4(arr) {
    let [a,b,c] = arr.slice(0,3);
    if( a != b && a != c ) return a;
    for( let x of arr ) if( x!=a ) return x
  }
