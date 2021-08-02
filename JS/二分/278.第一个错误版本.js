var solution = function(isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
     return function(n) {
        let left = 1;
         let right = n;
         
         // 循环一
        while (left < right) {
            let mid = left + Math.floor((right - left) / 2);
            if (isBadVersion(mid)) {
                right = mid;
            } else {
                left = mid+1;
            }
         }
         // 循环二
         while (left <= right) {
            let mid = left + Math.floor((right - left) / 2);
            if (isBadVersion(mid)) {
                right = mid-1;
            } else {
                left = mid+1;
            }
        }
        console.log(left, right)
        return left;
    };
};

console.log(solution(5)(4));