function random(low, high, count) {
    if (count >= high - low + 1) {
        console.log("impossible");
        return
    }
    let res = new Set();
    let s = 0;
    let randInt = 0;
    while (s < count) {
        randInt = low + Math.floor(Math.random() * (high + 1 - low));
        if (!res.has(randInt)) {
            res.add(randInt);
            s += 1;
        }
    }
    console.log(res);
}

function quickSort(nums, left, right) {
    if (left >= right) {
        return
    }
    let idx = find(nums, left, right);
    console.log(idx);
    // 排序哨兵的左边
    quickSort(nums, left, idx - 1);
    // 排序哨兵的右边
    quickSort(nums, idx + 1, right);
}

function find(nums, left, right) {
    // 选取最右的为哨兵
    let p = nums[left];
    let i = left;
    let j = left + 1;
    while (j <= right) {
        if (nums[j] <= p) {
            i += 1;
            [nums[i], nums[j]] = [nums[j], nums[i]];
        }
        j += 1;
    }
    // i的右边都是比p大的数，所以可以交换，这样i位置就是最终排序后的元素的位置
    [nums[i], nums[left]] = [nums[left], nums[i]];
    return i;
}
let a = [1, 6, 2, 4, 3];

quickSort(a, 0, 4)
console.log(a);

// random(1, 500, 6)