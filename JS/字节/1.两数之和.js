// 利用哈希值
var twoSum = function (nums, target) {
    let hash = {};
    for (let i = 0; i < nums.length; i++) {
        if ((target - nums[i]) in hash) {
            return [i, hash[target - nums[i]]]
        } else {
            hash[nums[i]] = i;
        }
    }
};

console.log(twoSum([1,7,3,5], 10));
console.log(twoSum([3,2,4], 6));
console.log(twoSum([3,3], 6));
console.log(twoSum([3], 3));