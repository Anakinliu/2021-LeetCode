// 下一个更大的排列
// 题目规定,必须 原地 修改，只允许使用额外常数空间。
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
// 参考: https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-suan-fa-xiang-jie-si-lu-tui-dao-/
// 这里是暴力版,作者写的是优化版
// 1. 先找需要最先互换的两个数,从后往前找,注意要是最小长度,找后N个数中排在第一的比较大的数
// 2. 交换两个元素
// 3. 升序排序叫喊后的后面的所有元素
var nextPermutation = function (nums) {
    let right;
    let left;
    let searchLen = nums.length - 2;
    // searchLen: 尽可能在右边找
    let flag = false;
    for (; searchLen >= 0; searchLen --) {
        right = nums.length - 1;
        for (; right > searchLen; right --) {
            left = right - 1;
            for (; left >= searchLen; left --) {
                if (nums[left] < nums[right]) {
                    flag = true;
                    break;
                }
            }
            if (flag) {
                break;
            }
        }
        if (flag) {
            break;
        }
    }
    console.log('lr', left, right);
    // 没有下一个更大的,题目要求返回升序数组
    if (!flag) {
        nums = nums.reverse();
        return
    }

    [nums[left], nums[right]] = [nums[right], nums[left]];

    let r_nums = nums.slice(left+1).sort((a,b) => a-b);
    for (let i = left+1; i < nums.length; i++) {
        nums[i] = r_nums[i-left-1];
    }

};

// let a = [3,2,1];
// let a = [1,3,5,3,2,1];
// let a = [1];
// let a = [1,1,5];
// let a = [2,2,7,5,4,3,2,2,1];  // [2,3,1,2,2,2,4,5,7]
// let a = [4,2,0,2,3,2,0]; // [4,2,0,3,0,2,2]
nextPermutation(a);
console.log(a);