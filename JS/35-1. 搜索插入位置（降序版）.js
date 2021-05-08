// TAG: array binary search
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
            high = mid - 1;
        } else if (nums[mid] > target) {
            low = mid + 1;
        }
        mid = Math.floor((low + high)/2);
    } 
    return low;

};


// 
console.log(searchInsert([6,5,3,1], 5)); // 1
console.log(searchInsert([6,5,3,1], 2)); // 3
console.log(searchInsert([6,5,3,1], 7)); // 0
console.log(searchInsert([6,5,3,1], 0)); // 4
console.log(searchInsert([2,1], 1)); // 0
console.log(searchInsert([2,1], 2)); // 1
console.log(searchInsert([1], 1)); // 0