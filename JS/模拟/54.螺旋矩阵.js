/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function (matrix) {
    let direction = 1;
    let count = 0;
    let m = matrix.length;
    let n = matrix[0].length;
    let level = 0;
    let resArr = [];
    while (count < m * n) {
        // 向右移动
        if (direction === 1) {
            for (let i = level; i <= n - level - 1; i++) {
                // console.log(matrix[level][i]);
                resArr.push(matrix[level][i]);
                count += 1;
            }
        }
        if (direction === 2) {
            for (let i = level + 1; i <= m - level - 1; i++) {
                // console.log(matrix[i][n - level - 1]);
                resArr.push(matrix[i][n - level - 1]);

                count += 1;
            }
        }
        if (direction === 3) {
            for (let i = n - level - 2; i >= level; i--) {
                // console.log(matrix[m - level - 1][i]);
                resArr.push(matrix[m - level - 1][i]);

                count += 1;
            }
        }
        if (direction === 4) {
            for (let i = m - level - 2; i >= level + 1; i--) {
                // console.log(matrix[i][level]);
                resArr.push(matrix[i][level]);
                count += 1;
            }
        }
        if (direction === 4) {
            level += 1;
            direction = 1;
        } else {
            direction += 1;
        }
    }
};

spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]);  // 3行3列
console.log("===");
spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]);  // 3行4列
console.log("===");
spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]); // 4行3列
console.log("===");
spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]); // 4行4列