/**
 * @param {character[][]} board
 * @return {boolean}
 */
// 三次遍历
var isValidSudoku = function (board) {
    // 验证一个数组中是否有重复的
    const hasRepet = (arr) => {
        let a = {};
        for (let e = 0; e < 9; e++) {
            if (arr[e] !== '.') {
                if (a[arr[e]]) {
                    console.log(arr);
                    return true;
                } else {
                    a[arr[e]] = 1;
                }
            }
        }
        return false;
    }
    let x = [0, 2];
    let y = [0, 2];
    // let y = [x[0]+2,]
    // console.log(validRow(["5", "3", ".", ".", "7", ".", ".", ".", "5"]));
    for (let i = 0; i < 9; i++) {
        if (i !== 0 && i % 3 === 0) {
            x[1] += 3;
            x[0] += 3;
            y[0] = 0;
            y[1] = 2;
        }
        console.log('---');
        console.log(board[i]);
        console.log(board.slice(0, board.length).map(j => j.slice(i, 1 + i)[0]));
        console.log([].concat(...board.slice(x[0], x[1] + 1).map(k => k.slice(y[0], y[1] + 1))));
        console.log('===');
        if (hasRepet(board[i])
            || hasRepet(board.slice(0, board.length).map(j => j.slice(i, 1 + i)[0]))
            || hasRepet([].concat(...board.slice(x[0], x[1] + 1).map(k => k.slice(y[0], y[1] + 1))))) {
            console.log(i);
            return false;
        }
        y[0] += 3;
        y[1] += 3;
    }
    // let cols = board.slice(0, board.length).map(i => i.slice(0, 1)[0]);
    // console.log(validRow(cols));
    // for (let i = 0; i < 9; i++) {
    //     if (!validRow(board[i])) {
    //         return false
    //     }
    // }
    return true;
};

let board =
    [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "."]];

// console.log([].concat(...board.slice(0, 2 + 1).map(k => k.slice(0, 2+1))))
// console.log(isValidSudoku(board));

// 一次遍历:
const solution = board => {

    let rows = [];
    let cols = [];
    let boxes = [];
    for (let i = 0; i < 9; i++) {
        rows.push({});
        cols.push({});
        boxes.push({});
    }

    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            const num = board[i][j];
            if (num !== '.') {
                const box_index = Math.floor(i / 3) * 3 + Math.floor(j / 3);
                if (rows[i][num] || cols[j][num] || boxes[box_index][num]) {
                    return false;
                } else {
                    rows[i][num] = 1;
                    cols[j][num] = 1;
                    boxes[box_index][num] = 1;
                }
            }
        }
    }
    return true;
}

console.log(solution(board));