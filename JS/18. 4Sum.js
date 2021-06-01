/**
 * @param {number[]} sortedNums
 * @param {number} target
 * @return {number[][]}
 */
// 固定左边 3 个指针，右边 1 个指针
var fourSum = function (nums, target) {
    const sortedNums = nums.sort((a, b) => a - b);
    let a = 0;
    const numsLen = sortedNums.length;
    const result = [];
    for (; a < numsLen - 3; a++) {
        let b = a + 1;
        for (; b < numsLen - 2; b++) {
            let c = b + 1;
            let d = numsLen - 1;
            while (c < d) {
                console.log(a,b,c,d);
                const sum4 = sortedNums[a] + sortedNums[b] + sortedNums[c] + sortedNums[d];
                if (sum4 < target) {
                    while (sortedNums[c] === sortedNums[c+1]) {
                        c += 1;
                    }
                    c += 1
                } else if (sum4 > target) {
                    while (sortedNums[d] === sortedNums[d-1]) {
                        d -= 1;
                    }
                    d -= 1
                } else {
                    result.push([sortedNums[a], sortedNums[b], sortedNums[c], sortedNums[d]]);
                    while (sortedNums[c] === sortedNums[c+1]) {
                        c += 1;
                    }
                    while (sortedNums[d] === sortedNums[d-1]) {
                        d -= 1;
                    }
                    c += 1;
                    d -= 1;
                }
            }
            while (sortedNums[b] === sortedNums[b+1]) {
                b += 1;
            }
        }
        while (sortedNums[a] === sortedNums[a+1]) {
            a += 1;
        }
    }
    return result;
};

// console.log(fourSum([1,1,1,1,1,1,1,1], 4));
console.log(fourSum([1,0,-1,0,-2,2], 0));
// -2, -1, 0, 0, 1, 2
console.log(fourSum([2,2,2,2,2], 8));