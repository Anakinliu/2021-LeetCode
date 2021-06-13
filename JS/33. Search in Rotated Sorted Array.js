/**
 * 题目数据保证按升序排列的 nums 在预先未知的某个下标上进行了旋转
 * 存在 log n 时间复杂度解法
 */
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number} 下标或-1
 */
// 1. 查找分界点
// 2. 对两个升序数组分别二分查找
var search = function (nums, target) {
    // return nums.indexOf(target);
    let idx = 1;
    while (nums[idx] && nums[idx - 1] < nums[idx]) {
        idx += 1;
    }
    // console.log(idx);
    const binarySearch = function (arr, target) {
        let low = 0;
        let high = arr.length - 1;
        let mid = Math.floor((low + high) / 2);

        while (low <= high) {
            if (arr[mid] === target) {
                return mid;
            }
            if (arr[mid] < target) {
                low = mid + 1;
            } else if (arr[mid] > target) {
                high = mid - 1;
            }
            mid = Math.floor((low + high) / 2);
        }
        // console.log('find');
        return -1;
    };
    console.log(nums.slice(idx));
    let res = binarySearch(nums.slice(idx), target);
    if (res >= 0) {
        return res + idx;
    } else {
        console.log(nums.slice(0, idx));
        return binarySearch(nums.slice(0, idx), target);;
    }
};

// 1. 从nums[0]和target判断target在nums[0]右边一半或者左边一半
// [左半段,右半段]
// 2. 转化为在一个有序数组中查找目标值
// 3. 看不懂
var search2 = function (nums, target) {
    let low = 0, high = nums.length - 1;
    while (low <= high) {
        let mid = Math.floor((high + low) / 2);
        if (target === nums[mid]) {
            return mid;
        }

        if (target >= nums[0]) {  // 目标值在左半段
            if (nums[mid] < nums[0]) {
                // 但是 mid 在右半段
                nums[mid] = Number.MAX_VALUE;
            }
        } else { // 目标值在右
            if (nums[mid] >= nums[0]) {
                // 但是 mid 在左半段
                nums[mid] = Number.MIN_VALUE;
            }
        }
        if (nums[mid] < target) {
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }

    }
    return -1;
}



console.log('res ', search([4, 5, 6, 7, 0, 1, 2], 2));
console.log('res ', search([1], 2));