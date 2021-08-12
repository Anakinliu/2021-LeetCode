var maxSubArray = function (nums) {
    let pre = 0;
    let maxAns = nums[0];
    for (let e of nums) {
        pre = Math.max(pre + e, e);
        maxAns = Math.max(maxAns, pre);
    }
    return maxAns;
};

// 带有数组的动态规划
/**
 * dp数组,dp[i]表示, 当nums[i]为连续数组的最后一个元素时的最大和子数组
 * 当i索引前一个dp[i-1]大于0时,dp[i]取dp[i-1] + nums[i]
 * 当i索引前一个dp[i-1]小于or等于0时,dp[i]取nums[i]
 */
var maxSubArray2 = function (nums) {
    let dp = Array(nums.length).fill(0);
    dp[0] = nums[0];
    let maxSum = dp[0];
    for (let i = 1; i < nums.length; i++) {
        dp[i] = dp[i - 1] > 0 ? dp[i-1] + nums[i] : nums[i];
        maxSum = Math.max(maxSum, dp[i]);
    }
    return maxSum;

}

// console.log(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]));
// console.log(maxSubArray([1]));
// console.log(maxSubArray([0]));
// console.log(maxSubArray([-999]));
// console.log(maxSubArray([-2, 1]));


console.log(maxSubArray2([-2, 1, -3, 4, -1, 2, 1, -5, 4]));
console.log(maxSubArray2([1]));
console.log(maxSubArray2([0]));

console.log(maxSubArray2([-999]));
console.log(maxSubArray2([-2, 1]));
