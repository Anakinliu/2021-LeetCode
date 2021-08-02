// left从1开始的写法:
function eatBan(arr, h) {
    // 求h所指向的目标是多少个
    function canEat(k) {
        let sumH = 0;
        for (let e of arr) {
            // e % k === 0 ? sumH += e / k : sumH += Math.ceil(e / k);
            sumH += Math.ceil(e / k);
        }
        return sumH > h;
    }
    let left = 1;  // 存在一种可能,立马吃完:arr=[5], h=4
    let right = Math.max(...arr);
    // console.log(low, high);
    while (left < right) {
        let mid = left + Math.floor((right - left) / 2);
        if (canEat(mid)) {  // 全吃了需要的时间sumH大于警卫休息时间h,吃不完,所以每次要多吃点,增加最小值
            left = mid + 1;
        } else {  // 需要的时间小于警卫休息时间,慢慢吃,缩减最大值
            right = mid;  // 因为最后解出的sumH会大于等于h,所以这里不要mid-1 !!!
        }
    }
    return left;
}

function eat2(arr, h) {
    function canEat(k) {
        let sumH = 0;
        for (let e of arr) {
            sumH += Math.ceil(e / k);
        }
        return sumH > h;
    }
    let left = 0;
    let right = Math.max(...arr) + 1;
    while (left !== (right - 1)) {
        let mid = Math.floor(left + (right - left) / 2);
        if (canEat(mid)) {
            left = mid;
        } else {
            right = mid;
        }
    }
    return right;
}

console.log(eat2([3, 6, 7, 11], 8));  // 4

