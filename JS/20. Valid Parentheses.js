/**
 * 只包含括号！！！
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  const stack = [];
  const map = {
    "(": ")",
    "[": "]",
    "{": "}",
  };
  for (let i = 0; i < s.length; i++) {
    if (map(s[i])) {
      stack.push(map(s[i]));
      continue;
    } else if (stack.pop() !== map(s[i])) {
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
var isValid = function (s) {
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

console.log(isValid("([])("));
console.log(isValid("(]"));
console.log(isValid("([)]"));
console.log(isValid("{[]}")); // TRUE
console.log(isValid("([}}[[]{}"));
