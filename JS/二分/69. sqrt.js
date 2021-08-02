function mySqrt(x) {
    if (x === 1) {
        return x;
    }
    let left = 2;
    let right = Math.floor(x / 2);
    while (left <= right) {
        let mid = left + Math.ceil((right - left) / 2);
        if (mid * mid > x) {
            right = mid - 1;
        } else if (mid * mid < x) {
            left = mid + 1;
        } else {
            return mid;
        }
    }
    // console.log(left, right);
    if (left === right) {
        console.log(x, ' left === right');
    }
    return right;  // 为什么是right?
}

// 把 mid*mid === x 与 mid*mid < x 融合
function mySqrt2(x) {
    if (x === 1) {
        return x;
    }
    let left = 2;
    let right = Math.floor(x / 2);
    let count = 0;
    while (left < right) {
        count += 1;
        let mid = Math.ceil(left + (right - left) / 2);
        if (mid * mid > x) {
            right = mid - 1;
        } else {
            left = mid;
        }
    }

    // while (left <= right) {
    //     count += 1;
    //     let mid = Math.floor(left + (right - left) / 2);
    //     if (mid * mid > x) {
    //         right = mid - 1;
    //     } else {
    //         left = mid + 1;
    //     }
    // }
    console.log("x = ", x, " count = ", count, "left: ", left, "right: ", right);
    return right;  // 为什么是right?
}

// console.log(mySqrt2(4));
for (let i = 2; i < 17; i++) {
    mySqrt2(i)
    // console.log(i, "sqrt(i): ", mySqrt2(i));
}