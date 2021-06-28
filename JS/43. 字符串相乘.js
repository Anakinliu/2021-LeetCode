/*
1. 不适用乘法

*/
var multiply = function (num1, num2) {
    // 有一个是"0"
    if (!+num1 || !+num2) return '0'

    // 乘积的最大长度
    const prod = Array(num1.length + num2.length).fill(0);
    let currIdx = prod.length - 1;

    for (let i = num1.length - 1; i >= 0; i--) {
        let idx = currIdx;

        for (let j = num2.length - 1; j >= 0; j--) {
            const res = +num1[i] * +num2[j] + prod[idx];
            prod[idx] = res % 10;  // 个位数
            prod[--idx] += Math.floor(res / 10);  // 十位数
            console.log(' ', res);
            console.log(' ', prod.join(''));
        }
        console.log(prod.join(''));
        currIdx -= 1;
    }
    console.log(prod.join(''));
    // 匹配以0开头的一个或多个
    return prod.join('').replace(/^0+/, '');
};

multiply("1234", "567");