# 最长回文子串,1 <= s.length <= 1000
# 我的暴力解法，超时GG
def longestPalindrome(s): 
    s_len = len(s)
    def isPal(s, n):
        for i in range(n//2):
            if s[i] != s[~i]:
                return False
        return True
    max_len = 1
    res = s[0]
    for i in range(s_len):
        for j in range(i+1, s_len):
            n = len(s[i:j+1])
            if n > max_len and isPal(s[i:j+1], n):
                    max_len = n
                    res = s[i:j+1]
    return res

# print(longestPalindrome("babad"))
# print(longestPalindrome("ac"))

# 尝试非暴力GG
def longestPalindrome2(s): 
    pass

"""
solution 1
最长公共子串

有人认为，反转S为S‘，对比S’与S的最长公共子串就是答案。
但是
S = "abacdfgdcaba", S'= "abacdgfdcaba".

最长公共子串是 "abacd". 不是回文串.
"""
def longestPalindrome3(s):
            

