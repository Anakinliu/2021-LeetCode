// 普通递归
// 正常递归版
function sumN(n) {
    if (n <= 0) {
        return 0;
    }
    return n + sumN(n - 1);
}

// 使用逻辑运算
function sumH(n) {
    return n > 0 && (n + (sumH(n - 1)));
}

// 套公式加位运算
function sumF(n) {
    return (Math.pow(n, 2) + n) >>> 1;
}

console.log(sumH(3));
console.log(sumN(3));
console.log(sumF(3));

// let x = -64;
// console.log(x >>> 1);  // 会去掉负号