// TAG: 二分搜索
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
 var searchInsert = function(nums, target) {
    // let index = -1;
    let low = 0;
    let high = nums.length - 1;
    let mid = Math.floor((low + high)/2);
    while (low <= high) {
        if (nums[mid] === target) {
            return mid;
        }
        if (nums[mid] < target) {
            low = mid + 1;
        } else if (nums[mid] > target) {
            high = mid - 1;
        }
        mid = Math.floor((low + high)/2);
    } 
    return low;

};
/*
示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0

*/
// 
console.log(searchInsert([1,3,5,6], 5)); // 2
console.log(searchInsert([1,3,5,6], 2)); // 1
console.log(searchInsert([1,3,5,6], 7)); // 4
console.log(searchInsert([1,3,5,6], 0)); // 0
console.log(searchInsert([1,2], 1)); // 0
console.log(searchInsert([1,2], 2)); // 1
console.log(searchInsert([1], 1)); // 0