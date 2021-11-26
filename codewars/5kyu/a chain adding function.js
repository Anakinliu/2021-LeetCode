function add(n) {
    // Let the currying begin!
    let res = n;
    function inner(m) {
        res += m;
        return inner
    }
    // inner[Symbol.toPrimitive] = function (hint) {
    //     return res
    // }
    // 也可以写valueOf
    inner.valueOf = () => {
        return res;
    }
    return inner;
}

console.log(add(1)(2)(3) == 6);

