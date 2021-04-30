// 行号从 0 开始
var getRow = function(numRows) {
    let pre = [1];

    let level = 0;
    while (level < numRows) {
        level += 1;
        let cur = [1];
        for (let i=1; i < level; i++) {
            // cur.push(pre[i] + pre[i-1]);
            cur[i] = (pre[i] + pre[i-1]);
        }
        cur.push(1);
        pre = cur;
    }
    return pre;
};

// @lzhoucs , 只需一个数组，从后向前不断更新
var getRow = function(numRows) {
    let arr = [1];

    for (let i = 1; i <= numRows; i++) {
        for (let j = i; j > 0; j--) {
            if (j == i) {
                arr[j] = 1;
            } else {
                arr[j] = arr[j-1] + arr[j];
            }
        }
    }
    return arr;
};