function quickSort(arr, l, r) {
    if (r <= l) {
        return
    }
    let q = partition(arr, l, r);
    console.log(q);
    quickSort(arr, l, q - 1);
    quickSort(arr, q + 1, r);
}

function partition(arr, l, r) {
    let p = r;  // 可以随机选取[l,r]内的值,这里选取最右作为哨兵索引
    // 将哨兵放到最右边,便于排序.
    // 由于这里选取的是r, 所以不用交换了
    // [arr[p], arr[r]] = [arr[r], arr[p]];
    let i = l;
    for (let j = l; j <= r - 1;) {
        if (arr[j] <= arr[r]) {
            [arr[i], arr[j]] = [arr[j], arr[i]];
            i += 1;
        } 
        j += 1;
    }
    // 交换哨兵和比哨兵大的元素,此时哨兵的位置就是最终位置了
    [arr[i], arr[r]] = [arr[r], arr[i]];
    return i;
}

let a = [1, 3, 5,3, 2, 4, 6,2,];
quickSort(a, 0, a.length-1);
console.log(a);