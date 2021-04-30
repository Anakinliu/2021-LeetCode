/**
 * @param {number[][]} grid
 * @return {number}
 */
 var minPathSum = function(grid) {
    let m = grid.length;
    let n = grid[0].length;
    let t = [];
    for (let j=0; j < m; j++) {
        let a = [];
        for (let i=0; i < n; i++) {
            a.push(0); 
        }
        t.push(a);
    }
    // console.log(t);
    t[0][0] = grid[0][0];
    for (let i=1; i < n; i++) {
        t[0][i] = grid[0][i] + t[0][i-1];
    }
    for (let i=1; i < m; i++) {
        t[i][0] = grid[i][0] + t[i-1][0];
    }
    console.log(grid);
    
    for (let i=1; i < m; i++) {
        for (let j=1; j < n; j++) {
            console.log(Math.min(t[i-1][j], t[i][j-1]), grid[i][j]);
            t[i][j] = Math.min(t[i-1][j], t[i][j-1]) + grid[i][j];
        }
    }
    console.log(t);
    return t[m-1][n-1];

};

console.log(minPathSum([[1,3,1],[1,5,1],[4,2,1]]));