/*
「不重复」的本质是什么？我们保持三重循环的大框架不变，只需要保证：

第二重循环枚举到的元素不小于当前第一重循环枚举到的元素；

第三重循环枚举到的元素不小于当前第二重循环枚举到的元素。

(a <= b <= c)保证了只有(a,b,c)会被枚举,而(b,a,c)和(c,b,a)则不会这就减少了重复
*/
var threeSum = function(nums) {
    nums.sort((a, b) => a - b);
    let len = nums.length;
    let res = [];
    for (let i = 0; i < len; i++) {

        if (i > 0 && nums[i] === nums[i - 1]) {
            continue;
        }

        for (let j = i + 1; j < len; j++) {
            if (j > i + 1 && nums[j] === nums[j - 1]) {
                continue;
            }
            for (let k = j + 1; k < len; k++) {
                if (k > j + 1 && nums[k] === nums[k - 1]) {
                    continue;
                }
                if (nums[i] + nums[j] === -nums[k]) {
                    res.push([nums[i], nums[j], nums[k]])
                }
            }
        }
    }
    return res;
};

/*
将第三重循环变成一个从数组最右端开始向左移动的指针
这个方法就是我们常说的「双指针」，当我们需要枚举数组中的两个元素时，
如果我们发现随着第一个元素的递增，第二个元素是递减的，
那么就可以使用双指针的方法，将枚举的时间复杂度从 O(N^2)减少至 O(N)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/3sum/solution/san-shu-zhi-he-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
*/
var threeSum2 = function (nums) {
    nums.sort((a, b) => a - b);
    let len = nums.length;
    let res = [];
    for (let i = 0; i < len; i++) {
        if (i === 0 || nums[i] !== nums[i - 1]) {
            let k = len - 1;
            for (let j = i + 1; j < len; j++) {
                if (j === i + 1 || nums[j] !== nums[j - 1]) {
                    while ((nums[i] + nums[j] + nums[k]) > 0 && k > j) {
                        k -= 1;
                    }
                    if ((nums[i] + nums[j] + nums[k]) === 0 && k > j) {
                        res.push([nums[i], nums[j], nums[k]]);
                    }
                }
            }
        }
    }
    return res;
};

// console.log(threeSum([-1, 0, 1, 2, 2, -1, -4, 4]));
// console.log(threeSum([1, 1, 1, 1, 1, 1, 1, 1, -2]));
// console.log(threeSum([]));
// console.log(threeSum([2, -2, 0]));
// console.log(threeSum([2, -2, 2, -2]));
console.log(threeSum([-4, -1, -1, 0, 1, 2]));
