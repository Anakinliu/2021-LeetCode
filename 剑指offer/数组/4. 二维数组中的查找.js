/**
 * 
 * @param {*} matrix 
 * @param {*} target 
 */
var findNumberIn2DArray = function (matrix, target) {

        if (matrix.length === 0 || matrix[0].length == 0)
            return false;
        const rows = matrix.length, cols = matrix[0].length;
        let r = 0, c = cols - 1; // 从右上角开始
        while (r <= rows - 1 && c >= 0) {
            if (target == matrix[r][c])
                return true;
            else if (target > matrix[r][c])
                r++;
            else
                c--;
        }
        return false;
};

findNumberIn2DArray([
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]);