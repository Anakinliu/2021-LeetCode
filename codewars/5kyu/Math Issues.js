/**
 * 实现函数，函数参数为非负数，不用考虑其他类型值
 */


// 我的解答
Math.round = function (number) {
    // 四舍五入
    const numStr = Array.from(String(number));
    const pointIdx = numStr.indexOf('.');
    if (pointIdx === -1) {
        return number;
    }
    const s = parseInt(numStr[pointIdx + 1]);
    let integer = parseInt(numStr.slice(0, pointIdx).join(''));
    if (s >= 5) {
        return integer + 1;
    } else {
        return integer;
    }
};

Math.ceil = function (number) {
    // 向上取整
    const numStr = Array.from(String(number));
    const pointIdx = numStr.indexOf('.');
    if (pointIdx === -1) {
        return number;
    }
    let integer = parseInt(numStr.slice(0, pointIdx).join(''));
    return integer + 1;
};

Math.floor = function (number) {
    // 向下取整
    const numStr = Array.from(String(number));
    const pointIdx = numStr.indexOf('.');
    if (pointIdx === -1) {
        return number;
    }
    let integer = parseInt(numStr.slice(0, pointIdx).join(''));
    return integer;
};


// 评论区大佬解答，我可真笨😁
Math.round2 = function (number) {
    // 四舍五入
    let m = parseInt(number) ;
    if (number >= m + 0.5) {
        return m + 1;
    } else {
        return m;
    }
};

Math.ceil2 = function (number) {
    // 向上取整
    if (number > parseInt(number)) {
        return parseInt(number) + 1;
    }
    return parseInt(number);
};

Math.floor2 = function (number) {
    // 向下取整
    return parseInt(number);
};


// console.log(Math.round(0.4));
// console.log(Math.round(0.5));
// console.log(Math.ceil(0.4));
// console.log(Math.ceil(0.5));
// console.log(Math.floor(0.4));
// console.log(Math.floor(0.5));