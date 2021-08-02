var maxSubArray = function (nums) {
    let pre = 0;
    let maxAns = nums[0];
    for (let e of nums) {
        pre = Math.max(pre + e, e);
        maxAns = Math.max(maxAns, pre);
    }
    return maxAns;
};

var maxSubArray2 = function (nums) {
    let maxAns = nums[0];
    for (let i = 0; i < nums.length; i++) {
        for (let j = i; j < nums.length; j++) {
            maxAns = Math.max(nums.slice(i, j + 1).reduce((a, b) => a + b, 0), maxAns);
        }
    }
    return maxAns;
}

// console.log(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]));
// console.log(maxSubArray([1]));
// console.log(maxSubArray([0]));
// console.log(maxSubArray([-999]));

console.log(maxSubArray2([-2, 1, -3, 4, -1, 2, 1, -5, 4]));
console.log(maxSubArray2([1]));
console.log(maxSubArray2([0]));

console.log(maxSubArray2([-999]));
console.log(maxSubArray2([-2, 1]));
