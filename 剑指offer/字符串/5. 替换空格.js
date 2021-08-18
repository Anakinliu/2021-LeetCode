const replaceSpace = function (str) {
    let reg = / /g;
    return str.replace(reg, "%20")
}

const replaceSpace2 = function (str) {
    let countSpace = 0;
    for (let c of str) {
        if (c === ' ') {
            countSpace += 1;
        }
    }
    // console.log('空格个数 ', countSpace);
    let strArr = Array.from(str).concat(Array(2 * countSpace));
    let left = str.length - 1;
    let right = strArr.length - 1;
    // console.log(left, right);
    while (left >= 0) {
        if (strArr[left] === ' ') {
            strArr[right--] = '0';
            strArr[right--] = '2';
            strArr[right--] = '%';
        } else {
            strArr[right] = strArr[left];
            right -= 1;
        }
        left -= 1;
    }
    return strArr.join('');
}

console.log(replaceSpace(" abc anc "));
console.log(replaceSpace2(" abc anc "));
console.log(replaceSpace("abcanc"));
console.log(replaceSpace2("abcanc"));
console.log(replaceSpace("abc    anc"));
console.log(replaceSpace2("abc    anc"));
console.log(replaceSpace(""));
console.log(replaceSpace2(""));
console.log(replaceSpace("    "));
console.log(replaceSpace2("    "));