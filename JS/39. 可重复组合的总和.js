/**
 * @param {number[]} candidates 所有数字（包括 target）都是正整数
 * @param {number} target
 * @return {number[][]}
 */
// 我的想法:
// 1. 两个指针,一个low=第一个, 一个last=最后一个
// 2. 如果 target % (low+last) == 0
//  如果 target % (low) == last
//  如果 target % (last) == low
//  如果 target % (last) == 0
//  如果 target % (low) == 0
// GG
// var combinationSum = function (arr, target) {
//     const sortedArr = arr.sort((a, b) => a - b);
//     let low = 0;
//     let high = arr.length - 1;
//     const res = [];
//     while (low <= high) {
//         if (target % (arr[low] + arr[high]) === 0) {
//             let t = [];
//             for (let i = 0; i < target / (arr[low] + arr[high]); i++) {
//                 t.concat([arr[low], arr[high]])                
//             }
//             res.push(t);
//         } else if (target % arr[low] === arr[high]) {

//         }
//     }
// };


// 回溯,力扣官方给的朴素回溯
var combinationSum = function (arr, target) {
    const lenLimit = arr.length;
    const resArr = []

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
        if (idx >= lenLimit || t < 0) {
            return
        }
        // 跳过当前索引,idx+1
        huisu(t, com, idx + 1);
        // 使用当前索引,由于每个元素都可以无限次使用,所以 idx 不需要 +1
        huisu(t - arr[idx], [...com, arr[idx]], idx);
    }
    huisu(target, [], 0);
    // console.log(resArr);
    return resArr;
};

// 回溯剪枝
// 1. 先对arr 排序
// 2. 当huisu内的t小于arr[idx]时,不用再往下找下去了,达到剪枝效果
var _combinationSum = function (arr, target) {
    const sortedArr = arr.sort((a, b) => a - b);
    let lenLimit = sortedArr.length - 1
    const resArr = []

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
            // 使用当前索引,由于每个元素都可以无限次使用,所以 idx 不需要 +1
            huisu(t - sortedArr[idx], [...com, sortedArr[idx]], idx);
        }

    }
    huisu(target, [], 0);
    console.log(resArr);
    return resArr;
};
// _combinationSum([2, 3, 7], 11);
// _combinationSum([2, 3, 6, 7], 7);
_combinationSum([2, 3, 5], 8);