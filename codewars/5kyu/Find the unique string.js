/**
 * 所有字符串都包含相似字符，除了唯一的一个
 * 
 * findUniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) === 'BbBb'
   findUniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) === 'foo'

   字符串会包含，空格视为无意义字符，"  "等同于空字符串""
   数组至少包含3个字符串
 */

/**
 * 我的提交
 */
function similar(a, b) {
    // 判断两个元素是否相似
    const c = Array.from(new Set(a.toLowerCase())).filter(e => e !== ' ').sort().join('');
    const d = Array.from(new Set(b.toLowerCase())).filter(e => e !== ' ').sort().join('');
    if (c === d) {
        return true;
    }
    if (c && d) {
        // 空字符串是任何字符串（包括自身）的子串
        if (c.includes(d) || d.includes(c)) {
            return true;
        }
    }
    console.log(false, `=${c}==${d}=`);
    return false;
}

function findUniq(arr) {
    // do magic
    let len = arr.length;
    let leftP = 0;
    let mostE, oneE = 0;
    // 主体分两种情况
    if (similar(arr[leftP], arr[len - 1])) {
        // 情况一，最左最右相等，则那个数在里面，挨个遍历
        mostE = arr[leftP];
        leftP++;
        while (leftP < len) {
            if (false === similar(arr[leftP], mostE)) {
                oneE = arr[leftP];
                break;
            }
            leftP++;
        }
    } else {
        // 情况二，不相等，必有一个是答案，直接对比第二个元素
        if (similar(arr[leftP], arr[leftP + 1])) {
            oneE = arr[len - 1];
        } else {
            oneE = arr[leftP];
        }
    }
    return oneE;
}

// console.log(findUniq(['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a']));
// console.log(findUniq(['abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba']));

// const a1 = ['', '', '', 'a', '', '']
// const a2 = ['    ', '  ', ' ', 'a', ' ', '']
// const a3 = ['foobar', 'barfo', 'fobara', '   ', 'fobra', 'oooofrab']
// console.log(findUniq(a1));
// console.log(findUniq(a2));
// console.log(findUniq(a3));


/**
 * 答案区大佬的
 */

function findUniq2(arr) {
     // 确定大多数，但是有可能找到特殊的那个
    let [a,b,c] = arr.slice(0,3)
    
    if (!similar(a,b) && !similar(a,c)) return a
    for (d of arr) if (!similar(a,d)) return d
  }
  
  function similar (x, y) {
    x = new Set(x.toLowerCase())
    y = new Set(y.toLowerCase())
  
    if (x.size !== y.size) return false
    for (z of x) if (!y.has(z)) return false
  
    return true
  }