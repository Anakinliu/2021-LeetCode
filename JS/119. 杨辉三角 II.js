/**
 * @param {number} rowIndex
 * @return {number[]}
 */
 var getRow = function(rowIndex) {
     ++rowIndex;
    if (rowIndex === 1) {
        return [1];
    }
    if (rowIndex === 2) {
        return [1,2];
    }
    let i = 3;
    let cur = [1,1];
    for (; i <= rowIndex; i++) {
        cur.push(1);
        for (let j=i-2; j >= 1; j--) {
            cur[j] = cur[j] + cur[j-1];
        }
    }
    return cur;
};

var getRow = function(rowIndex) {
    ++rowIndex;  //第一行的rowIndex为 1
    const row = new Array(rowIndex).fill(0);
    row[0] = 1;
    for (let i = 1; i < rowIndex; ++i) {
        row[i] = row[i - 1] * (rowIndex - i ) / i ;
    }
    return row;
};


console.log(getRow(200));
console.log(getRow(3));
