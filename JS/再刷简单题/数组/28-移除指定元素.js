var removeElement = function (nums, val) {
    // left从左边开始递增，寻找等于val的值
    let left = 0;
    /* 
    right从右边开始，找不等于val的值,注意right不是最后一个元素索引,
    而是数组长度,为什么?想象看只有一个元素的数组的情况
     */
    let right = nums.length;
    while (left < right) {
        if (nums[left] === val && nums[right - 1] !== val) {
            nums[left] = nums[right - 1];
            left += 1;
            right -= 1;
        }
        if (nums[left] !== val) {
            left += 1;
        }
        if (nums[right - 1] === val) {
            right -= 1;
        }
    }

    console.log(left, right, nums)
    // left指向的元素值是val,返回left+1
    return left;
};

console.log(removeElement([2], 2));
console.log(removeElement([2], 3));
console.log(removeElement([2, 2, 1], 2));
console.log(removeElement([3, 2, 2, 3], 3));