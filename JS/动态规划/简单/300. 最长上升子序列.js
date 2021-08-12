/**
 * @param {number[]} nums
 * @return {number}
 * 给定一个无序的整数数组，找到其中最长上升子序列的长度。
 * dp[i]表示[0-i]内的以i结尾的最长递增子序列长度
 */
var lengthOfLIS = function (nums) {
    let dp = Array(nums.length).fill(0);
    dp[0] = 1;
    // let pre = nums[0];
    for (let i = 1; i < nums.length; i++) {
        // 找出i前面的所有比nums[i]小的元素的索引对应的dp值
        let tempDp = dp.filter((_, idx) => {
            return idx < i && nums[idx] < nums[i];
        });
        if (tempDp.length) {
            // 这些索引中dp值大的加一就是dp[i]的值
            dp[i] = Math.max(...tempDp) + 1;
        } else {
            // 如果i元素就是最小的元素,则为1
            dp[i] = 1;
        }
    }
    return Math.max(...dp);
};

console.log(lengthOfLIS([0, 1, 0, 3, 2, 3]))
console.log(lengthOfLIS([1, 1, 1, 1, 1, 1, 1]))
console.log(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
