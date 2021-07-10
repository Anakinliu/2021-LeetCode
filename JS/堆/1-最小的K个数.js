function GetLeastNumbers_Solution(input, k) {
    // write code here
    if (k > input.length) {
        return [];
    }
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

        let min = i;
        const left = 2 * i + 1;
        const right = 2 * i + 2;
        // 比较其左右节点与自身的三个值,得到最大值
        if (left <= n && arr[left] < arr[min]) {
            min = left;
        }
        if (right <= n && arr[right] < arr[min]) {
            min = right;
        }
        if (min !== i) {
            swap(arr, i, min);
            heapify(arr, n, min);
        } else {
            return  // min就是i时不用解了,退出
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

    // 前 k 个
    function sortByHeap(arr, k) {
        buildHeap(arr);
        let n = arr.length - 1;
        const sortedArr = [];
        const stop = n - k;
        while (n > stop) {
            sortedArr.push(arr[0]);
            swap(arr, 0, n);
            // 不用截断数组, 直接把arr长度"改掉"
            heapify(arr, n - 1, 0);
            n -= 1;
        }
        return sortedArr;
    }
    // console.log(sortByHeap(input, k));
    return sortByHeap(input, k);
}

// const arr = [7, 9, 11, 15, 17, 6, 13];
// GetLeastNumbers_Solution(arr, 3)