/**
 * @param {number[]} nums
 * @return {number}
 */
/*
如果有多个位置通过跳跃都能够到达最后一个位置，那么我们应该如何进行选择呢？
贪心,从最后一步向前查找,找哪一个元素可以一步到达最后一个元素,需要从左向右查找,这样才能
找到距离最后一个元素最远的位置,
继续贪心地寻找倒数第二步跳跃前所在的位置，以此类推，直到找到数组的开始位置。
*/
var jump1 = function (nums) {
    let position = nums.length - 1;
    let step = 0;
    while (position > 0) {
        for (let i = 0; i < position; i++) {
            if (i + nums[i] >= position) {
                position = i;
                step += 1;
                break;
            }
        }
    }
    return step;
};


/*

*/
var jump = function (nums) {
    let step = 0;
    let maxPos = 0;
    let end = 0;  //边界,索引到达边界时更新步数和边界
    for (let i = 0; i < nums.length - 1; i += 1) {
        maxPos = Math.max(maxPos, nums[i] + i);
        console.log('maxPos', maxPos);
        // 边界内有更远的跳跃距离?那也得建立在这个元素在之前的跳跃距离内这个前提下
        // 所以,需要步数加1和更新边界
        if (i === end) {
            end = maxPos;
            step += 1;
        }
        console.log(step, i);
    }
    console.log(step);
    return step;
};

// jump([2, 3, 1, 1, 4]);
// jump([2, 3, 0, 1, 4]);
// jump([2, 1, 1, 1, 1, 1, 1, 1])
// jump([2, 1, 1, 1, 1])
// jump([2, 1])
// jump([2, 3, 1, 1, 4])
jump([1, 2, 1, 1, 1])