/**
 * 先固定一个数，再用两个指针遍历？
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
// Input: nums = [-1,2,1,-4], target = 1
var threeSumClosest = function (nums, target) {
    function sum(a,b,c) {
        return sortedNums[a] + sortedNums[b] + sortedNums[c];
    }
    const sortedNums = nums.sort((a, b) => a - b);
    console.log(sortedNums);
    let diff = Number.MAX_VALUE;
    let closestSum = Number.MAX_VALUE;
    for (let point = 0; point < nums.length - 2; point++) {
        let low = point + 1;
        let high = nums.length - 1;
        while (low < high) {
            const currDiff = sum(point, low, high) - target;
            console.log('currDiff ' + currDiff);
            if (currDiff < 0) {
                low += 1;
            } else if (currDiff > 0) {
                high -= 1;
            } else {
                return target;
            }
            if (Math.abs(currDiff) < diff) {
                diff = Math.abs(currDiff);
                closestSum = currDiff + target;
            }
        }
    }
    return closestSum;
};

console.log(threeSumClosest([0,1,2], 3)); 