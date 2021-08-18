/**
 * 时间复杂度 O(N)，空间复杂度 O(1)
 * @param {*} nums 
 */
var findRepeatNumber = function (nums) {
    let idx = 0;
    while (idx < nums.length) {
        
        if (idx != nums[idx]) {
            if (nums[idx] == nums[nums[idx]]) {
                return nums[idx];
            }
            [nums[nums[idx]], nums[idx]] = [nums[idx], nums[nums[idx]]];
        } else {
            idx++;
        }
    }

};
findRepeatNumber([2, 3, 1, 0, 2, 5])