/**
 * @param {number} x
 * @return {number}
 */
 var reverse = function(x) {
    // 直接字符串反转，会出现很多前置0的情况，此时对number的值直接调用Number转换会出现进制错误,要改为string类型再调用Number，就会自动忽略前置的0
    let z =  x;
    let arr = [];
    while (z !== 0) {
        arr.push(Math.abs(z % 10));
        z = parseInt(z / 10);
    }
    let temp = arr.join('');
    let res = Number(temp);
    res = x > 0 ? res : -res;
    if (res < -(2 ** 31) || res >= 2 ** 31) {
        return 0;
    }
    return res;
};