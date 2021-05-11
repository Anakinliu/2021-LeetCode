/**
 * @param {string} s
 * @return {boolean}
 */
 var isPalindrome = function(s) {
    s = s.toUpperCase();
    if (s === "") {
        return true;
    }
    let low = 0;
    let high = s.length - 1;
    while (low <= high) {
        if (!s[low].match(/[A-Z0-9]/)) {
            ++low;
            continue;
        }
        if (!s[high].match(/[A-Z0-9]/)) {
            --high;
            continue;
        }
        if (s[low] !== s[high]) {
            return false;
        }
        ++low;
        --high;
    }
    return true;
};

// console.log(isPalindrome("A man, a plan, a canal: Panama"));
// console.log(isPalindrome("race a car"));

// console.log(isPalindrome(" "));
// console.log(isPalindrome(";:,?aaabb,.,a.aaa"));
console.log(isPalindrome("0P"));
