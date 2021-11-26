var removeDuplicates = function (nums) {
    // nums是升序的
    // 使用两个指针解决。
    // idx1指向不重复的元素的索引
    let idx1 = 0;
    let idx2 = 1;
    while (idx2 < nums.length) {
        if (nums[idx2] === nums[idx1]) {
            idx2 += 1;
        } else {
            idx1 += 1;
            nums[idx1] = nums[idx2];
        }
    }
    return idx1 + 1;
};