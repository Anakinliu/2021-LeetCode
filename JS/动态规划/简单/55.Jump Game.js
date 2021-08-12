/**
 * @param {number[]} nums 数组元素最少一个,元素是非负整数
 * @return {boolean}
 */
// 子问题是,看能不能跳到i位置,i位置跳不到,后面的必定更跳不到
// 由于初始站在索引0位置,所以0位置是可以跳到的.即dp[0] = 0
// dp[i] 表示子数组[0,i]内可跳的最远的位置
// 当索引到k,分两种情况:
// 1. k > dp[k - 1], 则此k索引位置不可达,后面更不能到达,退出返回false
// 2. 更新dp[k]后,若dp[k]已经包含最大索引,则返回true
var canJump = function (nums) {
    // if (nums.length === 1) {
    //     return true;
    // }
    let dp = Array(nums.length).fill(0);
    dp[0] += nums[0];
    let i = 1;
    for (; i < nums.length; i++) {
        if (i > dp[i - 1]) {
            console.log('此时 i 为 ', i);
            return false;
        }
        dp[i] = Math.max((i + nums[i]), dp[i - 1]);
        console.log(dp[i]);
        if (dp[i] >= nums.length - 1) {
            return true;
        }
    }
    // 只有一个元素的情况直接返回true
    return true
};
// console.log(canJump([1, 2, 3, 4]));
// console.log(canJump([1, 2, 3]));
// console.log(canJump([1, 2, 3, 4, 0, 0, 0, 0, 0]));
console.log(canJump([1]));
// console.log(canJump([2, 3, 1, 1, 4]));
console.log(canJump([3, 2, 1, 0, 4]));