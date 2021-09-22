/*
跟踪到目前为止放置的左括号和右括号的数目

*/
function generate(n) {
    let ans = []
    // s是生成的字符串,每次递归都要更新
    // left是左括号的数目
    // right是右括号的数目
    function _gen(s, left, right) {
        if (s.length === n * 2) {
            ans.push(s);
            return
        }
        if (left < n) {
            _gen(s + '(', left + 1, right);
        }
        if (left > right) {
            _gen(s + ')', left, right + 1);
        }
    }
    _gen('', 0, 0)
    return ans.join(',')
}
console.log(generate(3));
