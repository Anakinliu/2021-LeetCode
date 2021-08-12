/*
题目“最长上升子序列” 以及 "最大子序和"，学习了DP（动态规划）在线性
关系中的分析方法。这种分析方法，也在运筹学中被称为“线性动态规划”，具体指的是 “目标函数
为特定变量的线性函数，约束是这些变量的线性不等式或等式，目的是求目标函数的最大值或最
小值”。
*/

/*
此题略微区别于之前的题型，
希望可以由此题与之前的题目进行对比论证，进而顺利求解！
*/
/**
 * @param {number[][]} triangle
 * @return {number}
 */
var minimumTotal = function (triangle) {
    let n = triangle.length;
    let dp = Array(n).fill(0);
    dp[0] = triangle[0][0];
    // 从后向前更新!
    for (let i = 1; i < n; i++) {
        // 行的最后一个
        dp[i] = dp[i - 1] + triangle[i][i];
        for (let j = i - 1; j >= 1; j--) {
            dp[j] = Math.min(dp[j], dp[j - 1]) + triangle[i][j];
        }
        // 行的第一个
        dp[0] = dp[0] + triangle[i][0];

        // console.log(dp);
    }
    return Math.min(...dp);
};

// console.log(minimumTotal([[1]]));
console.log(minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]));