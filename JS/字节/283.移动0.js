var moveZeroes = function (nums) {
    // left指向0元素
    // right指向非0元素
    // 交换后,left需要更新
    let left = 0;
    while (nums[left] !== 0 && left < nums.length) {
        left += 1;
    }
    let right = left + 1;
    while (right < nums.length) {
        if (nums[right] !== 0) {
            [nums[right], nums[left]] = [nums[left], nums[right]];
            // 两个0挨着,不挨着,两种情况,left都是加1,所以不用while循环寻找0元素
            left += 1;
        }
        right += 1;
    }
};

let arr = [0, 1, 3, 0, 6, 4];
moveZeroes(arr)
console.log(arr);