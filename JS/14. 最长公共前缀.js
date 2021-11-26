var longestCommonPrefix = function (strs) {
    let minL = strs[0].length;

    for (let w of strs) {
        minL = w.length < minL ? w.length : minL;
    }
    console.log(minL)

    if (minL < 1) {
        return ""
    }
    let i = 0;
    for (; i < minL; i++) {
        let char = strs[0][i];
        for (let w of strs) {
            if (w[i] !== char) {
                return w.substring(0, i);
            }
        }
    }
    console.log(i);

    if (i > 0) {
        return strs[0].substring(0, i);
    }
    return strs[0];
};
console.log(longestCommonPrefix(
    ["cbab", "aba", "eft"]));