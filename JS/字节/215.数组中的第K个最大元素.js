var findKthLargest = function (arr, k) {
    let l = 0;
    let r = arr.length - 1;
    while (l <= r) {
        let q = partition(arr, l, r);
        if (q + k === arr.length) {
            return arr[q];
        } else if (q + k < arr.length) {
            l = q + 1;
        } else {
            r = q - 1;
        }
    }
}

function partition(arr, l, r) {
    let p = r;  // 可以随机选取[l,r]内的值
    // 由于这里选取的是r,所以不用交换了
    // [arr[p], arr[r]] = [arr[r], arr[p]];
    /**
     * [i,j)为大于arr[p]的
     * [l,i)为小于arr[p]的
     */
    let i = l;
    let j = l;
    for (j = l; j <= r - 1;) {
        if (arr[j] <= arr[p]) {
            [arr[i], arr[j]] = [arr[j], arr[i]];
            i += 1;
        }
        j += 1;

    }
    // 别忘了这一步
    [arr[i], arr[r]] = [arr[r], arr[i]];
    return i;
}

console.log(findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4));
console.log(findKthLargest([3, 2, 1, 5, 6, 4], 7));