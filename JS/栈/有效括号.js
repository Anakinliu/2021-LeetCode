var isValid = function (s) {
    let stack = [];
    let m = {
        ')': '(',
        '}': '{',
        ']': '[',
    }
    let k = '[{(';
    for (let p of s) {
        // 左括号放入栈
        if (k.indexOf(p) !== -1) {
            stack.push(p);
        } else {
            // 右括号出栈如果不匹配,返回false
            if (stack.length === 0 || m[p] !== stack.pop()) {
                return false
            }
        }
    }
    // 剩余多余括号,false
    if (stack.length) {
        return false
    }
    return true
};

// console.log(isValid('[]{}'));
console.log(isValid('()'));