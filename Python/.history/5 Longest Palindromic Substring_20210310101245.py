# 最长回文子串,1 <= s.length <= 1000
# 我的暴力解法
def longestPalindrome(s):
    s_len = len(s)
    for i in range(s_len):
        for j in range(s_len-1)