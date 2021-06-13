/**
 * @param {number} n
 * @return {string[]}
 */
// 参考:  https://leetcode-cn.com/problems/generate-parentheses/solution/hui-su-suan-fa-by-liweiwei1419/
var generateParenthesis1 = function (n) {
    const res = [];
    function p(left, right, str) {
        if (left === 0 && right === 0) {
            res.push(str);
            return
        }
        if (left > 0 || right > 0) {
            if (left > 0) {
                p(left - 1, right, str + "(");
            }
            if (right > left) {
                p(left, right - 1, str + ")");
            }
        }
    }
    p(n, n, "");
    // console.log(res);
    return res;
};

var generateParenthesis2 = function (n) {
    // 1. 左 === 右, 添加到 res, return
    // 2. 左 <= n, 添加左括号
    // 3. 左 > 右时才添加 右括号
    const res = [];
    function p(left, right, str) {
        if (left === n && right === n) {
            res.push(str);
            return
        }
        if (left <= n) {
            p(left + 1, right, str + "(");
        }
        if (right < left) {
            p(left, right + 1, str + ")");
        }

    }
    p(0, 0, "");
    // console.log(res);
    return res;
};

generateParenthesis2(2);