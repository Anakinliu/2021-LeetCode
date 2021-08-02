/**
 * 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

s 由英文字母、数字、符号和空格组成

 */

/**
 * 滑动窗口⭐⭐⭐⭐⭐

什么是滑动窗口？

其实就是一个队列,比如例题中的 abcabcbb，进入这个队列（窗口）为 abc 满足题目要求，
当再进入 a，队列变成了 abca，这时候不满足要求。所以，

我们只要把队列的左边的元素移出就行了，直到队列内不再包含重复的字符!
一直维持这样的队列，找出队列出现最长的长度时候，求出解！

作者：powcai
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/hua-dong-chuang-kou-by-powcai/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
 */

var lengthOfLongestSubstring = function (s) {
    let q = [];
    let maxAns = 0;
    for (let e of s) {
        let idx = q.indexOf(e, 0);
        if (idx !== -1) {
            maxAns = Math.max(maxAns, q.length);
            q = q.slice(idx + 1);  //直接截取数组,一个个出队也可以
        } 
        q.push(e);
    }
    return Math.max(maxAns, q.length);
};

console.log(lengthOfLongestSubstring("abcabcbb"));  // 3
console.log(lengthOfLongestSubstring("bbbbb"));  // 1
console.log(lengthOfLongestSubstring("pwwkew")); // 3
console.log(lengthOfLongestSubstring(""));  // 0
console.log(lengthOfLongestSubstring("aab"));  // 2