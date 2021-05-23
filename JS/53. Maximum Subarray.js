/**
 * @param {number[]} nums
 * @return {number}
 */

// 动态规划
var maxSubArray = function (nums) {
  let [pre, res] = [0, nums[0]];
  nums.forEach((e) => {
    pre = Math.max(pre + e, e);
    res = Math.max(res, pre);
  });
  return res;
};

// 动态规划2
var maxSubArray2 = function (nums) {
  const t = [nums[0]];
//   let res = t[0];
  for (let i=1; i<nums.length; ++i) {
    t.push(Math.max(t[i-1] + nums[i], nums[i]));
    // res = Math.max(res, t[i]);
  }
//   return res;
  return Math.max(...t);
};

console.log(maxSubArray2([-2, 1, -3, 4, -1, 2, 1, -5, 4]));
console.log(maxSubArray2([1]));
console.log(maxSubArray2([-2, -5]));
console.log(maxSubArray2([5, 4, -1, 7, 8]));
