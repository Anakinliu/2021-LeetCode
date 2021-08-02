function is2(n) {
    if (n <= 0) {
        return false;
    }
    while (true) {
        if (n === 1) {
            return true;
        }
        if (n & 1 === 1) {
            // 说明n的二进制表示中最后一个二进制位是1
            return false;
        }
        n = n >>> 1;
    }
}

var isPowerOfTwo = function(n) {
    return n > 0 && (n & (n-1)) === 0;
};


for (let i = 1; i < 100; i++) {
    if (is2(i)) {
        console.log(i);
    }
}