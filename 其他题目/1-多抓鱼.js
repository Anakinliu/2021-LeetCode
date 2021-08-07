function solu(nums, money) {
    // 数组升序排序
    nums.sort((a, b) => a - b);
    let left;
    let right = nums.length;
    let count = 0;
    for (left = 0; left < right;left++) {
        for (let j = left + 1; j < right; j++) {
            if (nums[left] + nums[j] > money) {
                right = j;
                break;
            } else {
                count = (count + 1) % 1000000007;
            }
        }
    }
    console.log('result count: ', count);
    return count;
}

solu([5, 2, 3, 5], 6)
solu([3, 3, 3, 3], 6)
solu([3, 3], 6)