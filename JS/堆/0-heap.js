function swap(arr, i, j) {
    const temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}

// 从一个节点,开始自上至下
function heapify(arr, n, i) {
    // n: 使用的arr长度,从0开始
    // i: 当前节点的索引位置
    // arr: 一维数组表示的堆

    // 递归的结束条件
    if (i >= n) {
        return;
    }

    let max = i;
    const left = 2 * i + 1;
    const right = 2 * i + 2;
    // 比较其左右节点与自身的三个值,得到最大值
    if (left <= n && arr[left] > arr[max]) {
        max = left;
    }
    if (right <= n && arr[right] > arr[max]) {
        max = right;
    }
    if (max !== i) {
        swap(arr, i, max);
        heapify(arr, n, max);
    } else {
        return  // max就是i时不用解了,退出
    }
}

function buildHeap(arr) {
    // 需要借助heapify方法
    let last = arr.length - 1;
    last = Math.floor((last - 1) / 2);
    while (last >= 0) {
        heapify(arr, arr.length - 1, last);
        last -= 1;
    }
}

function sortByHeap(arr) {
    buildHeap(arr);
    let n = arr.length - 1;
    const sortedArr = [];
    while (n >= 0) {
        sortedArr.push(arr[0]);
        swap(arr, 0, n);
        // 不用截断数组, 直接把arr长度"改掉"
        heapify(arr, n - 1, 0);
        n -= 1;
    }
    return sortedArr;
}

(() => {
    const arr = [4, 10, 3, 5, 1, 2];
    heapify(arr, 6, 0);
    console.log(arr);
})();

(() => {
    const arr = [7, 9, 11, 15, 17, 6, 13];
    buildHeap(arr);
    console.log(arr);
})();

(() => {
    const arr = [7, 9, 11, 15, 17, 6, 13];
    console.log(sortByHeap(arr));
})();



