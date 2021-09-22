/**
 * 
 * 给定一个正整数数组,寻找数组中重复次数第N多的数字和对应的重复次数.
 * 重复次数一致,则较小的在前,若N没有对应的数字,则输出-1
 * 
 * 输入:数组,重复第N多的N
 * 输出:结果元素,实际重复次数
 */
function solu(arr, times) {
    // arr.sort((a, b) => a - b);
    // console.log(arr);
    let map = {}
    for (let e of arr) {
        if (map.hasOwnProperty(e)) {
            map[e] += 1
        } else {
            map[e] = 1;
        }
    }
    let appear = [];
    for (let e of Object.keys(map)) {
        appear.push(Number(map[e]));
    }
    appear.sort((a, b) => b - a);
    let appearN = appear[times - 1];
    // console.log(map);
    // console.log(appear);
    // console.log(appearN);
    let res = [];
    for (let e of Object.keys(map)) {
        if (appearN === Number(map[e])) {
            res.push([Number(e), Number(map[e])]);
        }
    }
    
}
solu([1, 3, 2, 3, 2, 2, 1, 2], 1)
solu([1, 3, 2, 3, 2, 2, 1, 2], 2)