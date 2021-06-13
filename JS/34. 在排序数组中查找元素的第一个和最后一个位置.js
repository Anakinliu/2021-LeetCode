/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
// 1. 正常二分查找,找到一个等于target的index
// 2. 两个指针前后扩张,确定范围
 var searchRange = function(nums, target) {
    let searchTarget = function() {
        let low = 0;
        let high = nums.length - 1;
        let mid;
        while (low <= high) {
            mid = Math.floor((high + low) / 2);
            if (nums[mid] === target) {
                return mid;
            }
            if (nums[mid] > target) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        if (nums[mid] === target) {
            return mid
        }
        return -1;
    }
    // console.log(searchTarget());
    let mid = searchTarget()
    if (mid < 0) {
        return [-1, -1];
    }
    let low = high = mid;
    while (nums[low - 1] === target) {
        low -= 1;
    }
    while (nums[high + 1] === target) {
        high += 1;
    }
    return [low, high];
};




console.log(searchRange([5,7,7,8,8,10], 5));
console.log(searchRange([5,7,7,8,8,10], 6));
console.log(searchRange([], 6));