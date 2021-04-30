// 二进制（子集）枚举
/*

我们用一个 9 位二进制数 mask 来记录当前所有位置的状态，从第到高第 i 位为 0 表示 i 不被选择到子集中，为 1 表示 i 被选择到子集中。
不管输入是什么，平均都会会枚举 2 的 9 次方 次
*/
var combinationSum3 = function(k, n) {
    let temp = [];
    const ans = [];
    const check = (mask, k, n) => {
        temp = [];
        for (let i=0; i < 9; ++i) {
            // 检查当前位是否为 1
            if ((1 << i) & mask) {
                temp.push(i+1);
            }
        }
        // 使用的数的个数是否与 k 一致 
        // 且
        // 和是否与 n 一致
        return temp.length === k && temp.reduce((a,b) => a + b, 0) === n;
    };
    // 循环 2 的 9 次方 次
    // mask 中为 1 的位表示使用， 为 0 的位表示不使用
    for (let mask = 0; mask < (1 << 9); ++mask) {
        if (check(mask, k, n)) {
            ans.push(temp);
        }
    }

    return ans;
};