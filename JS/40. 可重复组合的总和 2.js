/*
1. 所有数字（包括目标数）都是正整数。
2. 数字不能重复使用
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */

var combinationSum2 = function (arr, target) {
    const sortedArr = arr.sort((a, b) => a - b);
    let lenLimit = sortedArr.length - 1
    let resArr = []

    const huisu = function (t, com, idx) {
        /*
        t: 当前target
        com: 当前组合
        idx: arr下标
         */
        // 找到一个和为t的组合
        if (t === 0) {
            resArr.push(com)
            return
        }
        // idx超过arr长度或者目标值不正确了
        if (idx > lenLimit || t < 0) {
            return
        }
        if (t >= arr[idx]) {
            // 跳过当前索引,idx+1
            huisu(t, com, idx + 1);

            huisu(t - sortedArr[idx], [...com, sortedArr[idx]], idx + 1);
        }

    }
    huisu(target, [], 0);
    // console.log(resArr);
    resArr = resArr.filter((val, idx, arr) => {
        let res = true;
        arr.forEach((e, eIdx) => {
            if (eIdx > idx && JSON.stringify(val) === JSON.stringify(e)) {
                res = false;
            }
        });
        return res;
    })
    // console.log(resArr);
    return resArr;
};



// 1. 相比39提的难点: 如何避免重复?
/*
这个方法最重要的作用是，可以让同一层级，不出现相同的元素。即
                  1
                 / \
                2   2  这种情况不会发生 但是却允许了不同层级之间的重复即：
               /     \
              5       5
                例2
                  1
                 /
                2      这种情况确是允许的
               /
              2  

*/


console.log(combinationSum2([10, 1, 2, 7, 6, 1, 5], 8));
console.log(combinationSum2([2, 5, 2, 1, 2], 5));