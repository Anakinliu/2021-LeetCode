/**
 * 只包含括号的字符串，检查括号是否正确匹配
 * @param {string} s，"([])("
 * @return {boolean}
 */
var isValid1 = function (s) {
  const stack = [];
  const map = {
    "(": ")",
    "[": "]",
    "{": "}",
  };
  for (let i = 0; i < s.length; i++) {
    if (map[s[i]]) {
      stack.push(map[s[i]]);
      continue;
    } else if (stack.pop() !== s[i]) {
      return false;
    }
  }
  return !stack.length;
};

/**
 * @author lanshunfang
 * @param {*} s
 * @returns
 */
var isValid2 = function (s) {
  const stack = [];
  const map = {
    "(": ")",
    "[": "]",
    "{": "}",
  };

  for (let i = 0; i < s.length; i++) {
    let c = s[i];
    if (map[c]) {
      stack.push(map[c]); //放入的是右半
    } else if (c !== stack.pop()) {
      return false;
    }
  }

  return !stack.length;
};

console.log(isValid1("([])("));
console.log(isValid1("(]"));
console.log(isValid1("([)]"));
console.log(isValid1("{[]}")); // TRUE
console.log(isValid1("([}}[[]{}"));
