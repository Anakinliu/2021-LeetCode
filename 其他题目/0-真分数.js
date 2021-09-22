// 最接近输入的a的真分数,a范围是[0.01, 0.99]
function solu(n) {
    let close = Number.MAX_VALUE;
    let res1 = 0;  // 最终结果分子
    let res2 = 0;  // 最终结果分母
    // 分母为i
    for (let i = 1; i <= 200; i++) {
        // 求分子
        let left = 1;
        let right = i;
        let mid;
        while (left < right) {
            mid = left + Math.floor((right - left) / 2);
            if (Math.abs(mid / i - n) < close) {
                close = Math.abs(mid / i - n);
                res1 = mid;
                res2 = i;
            }
            if ((mid / i) > n) {
                right = mid - 1;
            } else if ((mid / i) < n) {
                left = mid + 1;
            } else {
                // console.log('相等!');
                return [mid, i]
            }
            // console.log(left, right);
        }
    }
    return [res1, res2];
}
// console.log(solu(0.333333));
console.log(solu(0.01));
console.log(solu(0.99));
// console.log(solu(0.1415926535898));