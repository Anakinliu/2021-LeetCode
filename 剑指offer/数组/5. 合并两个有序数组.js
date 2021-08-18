// 假设,a1数组长度等于a1+a2之和
// m是a1中实际元素的数量
// n是a2中实际元素的数量

function merge(a1, m, a2, n) {
    let left1 = m - 1;
    let left2 = n - 1;
    let right = m + n - 1;
    while (left1 >= 0 && left2 >= 0) {
        if (a1[left1] < a2[left2]) {
            a1[right] = a2[left2];
            left2 -= 1;
        } else {
            a1[right] = a1[left1];
            left1 -= 1;
        }
        right -= 1;
    }
    console.log('left2, right', left2, right);
    while (left2 >= 0) {
        a1[right] = a2[left2];
        left2 -= 1;
        right -= 1;
    }
}

let a1 = [1, 3, 5, 0, 0, 0];
let a2 = [20, 22, 24];
merge(a1, 3, a2, 3);
console.log(a1);