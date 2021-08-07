/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function (nums1, nums2) {
    let res = new Set();
    for (let e of nums1) {
        if (nums2.indexOf(e) !== -1) {
            res.add(e);
        }
    }
    return Array.from(res);
};

console.log(intersection([1, 2, 2], [2, 3, 4]));
console.log(intersection([4, 9, 5], [9, 4, 9, 8, 4]));

//假设两个数组已经排序,可以使用两个指针分别指向数组第一个元素
function intersection2(nums1, nums2) {
    nums1 = nums1.sort((a, b) => a - b);
    nums2 = nums2.sort((a, b) => a - b);
    let a = 0, b = 0;
    let res = [];
    while (a < nums1.length && b < nums2.length) {
        if (nums1[a] === nums2[b]) {
            res.push(nums1[a]);
            while (a < nums1.length - 1 && nums1[a + 1] === nums1[a]) {
                a += 1;
            }
            a += 1;
            while (b < nums2.length - 1 && nums2[b + 1] === nums2[b]) {
                b += 1;
            }
            b += 1;
        } else if (nums1[a] > nums2[b]) {
            b += 1;
        } else {
            a += 1;
        }
    }
    return res;
}

console.log(intersection2([1, 2, 2], [2, 3, 4]));
console.log(intersection2([4, 9, 5], [9, 4, 9, 8, 4]));
