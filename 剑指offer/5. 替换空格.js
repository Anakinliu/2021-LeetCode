const replaceSpace = function (str) {
    let reg = / /g;
    return str.replace(reg, "%20")
}

console.log(replaceSpace(" abc anc "));