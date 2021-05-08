/** TAG:字符串
 * @param {string} s
 * @return {number}
 */
 var lengthOfLastWord = function(s) {
    let last = s.length - 1;
    let count = 0;
    while (s[last] === ' ') {
        --last;
    }
    while (!(s[last] === ' ') && last >= 0) {
        ++count;
        --last;
    }
    return count;
};

/**
 * 
示例 1：

输入：s = "Hello World"
输出：5
示例 2：

输入：s = " "
输出：0
 */
console.log(lengthOfLastWord("Hello World"));
console.log(lengthOfLastWord(" "));
console.log(lengthOfLastWord("bbb aa"));
console.log(lengthOfLastWord("bbb aa "));
console.log(lengthOfLastWord(" bbb aa"));
console.log(lengthOfLastWord(" bbb aa "));
console.log(lengthOfLastWord("aa"));
console.log(lengthOfLastWord("aa "));
console.log(lengthOfLastWord(" aa"));
console.log(lengthOfLastWord(" aa "));

