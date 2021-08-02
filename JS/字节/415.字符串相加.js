/**
 * num1 和num2 的长度都小于 5100
num1 和num2 都只包含数字 0-9
num1 和num2 都不包含任何前导零
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 * @param {*} num1 
 * @param {*} num2 
 */
var addStrings = function (num1, num2) {

    let aLen = num1.length - 1;
    let bLen = num2.length - 1;
    let res = [];  // 两个元素相加的和
    let jin = 0;  //进位
    while (aLen >= 0 && bLen >= 0) {
        let s = Number(num1[aLen]) + Number(num2[bLen]) + jin;
        jin = s >= 10 ? 1 : 0;
        res.push(s % 10)
        aLen -= 1;
        bLen -= 1;
    }
    console.log(jin);
    while (aLen >= 0) {
        let s = Number(num1[aLen]) + jin;
        jin = s >= 10 ? 1 : 0;
        res.push(s % 10);
        aLen -= 1;
    }
    while (bLen >= 0) {
        let s = Number(num2[bLen]) + jin;
        jin = s >= 10 ? 1 : 0;
        res.push(s % 10);
        bLen -= 1;
    }
    if (jin) {
        res.push(jin);
    }
    return res.reverse().join('');
    console.log(res.reverse().join(''));
    //  1234
    // 12345

};

addStrings('999999999999', '999');