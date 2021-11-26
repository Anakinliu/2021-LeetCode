/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
    /*
    官方题解：利用常数的额外存储。
    避免反转后的数溢出问题：得到输入的一半长度的数即可！
    怎么做？由于整个过程我们不断将原始数字除以 10，然后给反转后的数字乘上 10，所以，当原始数字小于或等于反转后的数字时，就意味着我们已经处理了一半位数的数字了。
    */
    if (x < 0) {
        return false;
    }
    // 反转一半，比较两半数是否相同。
    let z = 0;
    let xx = x;
    while (z < xx) {
        z = z * 10 + xx % 10;
        // 说明输入的数结尾是0，那么输入不可能是回文了。
        if (z === 0) {
            return false;
        }
        // 输入是奇数长度时
        if (z === xx) {
            return true;
        }
        xx = parseInt(xx / 10);
    }
    // 输入是偶数长度或者输入===0
    if (z === xx) {
        return true;
    }
    return false;
};