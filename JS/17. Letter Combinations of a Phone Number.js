/**
 * @param {string} digits
 * @return {string[]}
 */
// @腐烂的橘子 https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/solution/hui-su-dui-lie-tu-jie-by-ml-zimingmeng/
// 回溯  ， 当题目中出现 “所有组合” 等类似字眼时，我们第一感觉就要想到用回溯。
var letterCombinations = function (digits) {
    if (!digits) {
        return [];
    }
    const buttons = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    function backtrack(com, nextdigit) {
        if (nextdigit.length === 0) {
            res.push(com)
        } else {
            buttons[nextdigit[0]].forEach(element => {
                backtrack(com + element, nextdigit.slice(1));
            });
        }
    }
    const res = [];
    backtrack("", digits);
    return res;
};
var letterCombinations2 = function (digits) {
    if (!digits) {
        return [];
    }
    const buttons = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    };
    const que = [""];
    digits.split("").forEach(digit => {
        que.forEach(char => {

        })
    })
}

// @腐烂的橘子 
// 队列版


