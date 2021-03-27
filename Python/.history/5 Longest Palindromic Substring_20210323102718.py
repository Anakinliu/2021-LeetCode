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
    pass


"""
solution 3

中心扩展算法
"""
def longestPalindrome5(s):
    res = ""

    # 以left，right为起始的最大可扩展长度，最长的回文长度
    def expandCheck(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1
        
    for idx in range(len(s)):  # 从第一个字符开始枚举
        # 奇数长
        l1, r1 = expandCheck(s, idx, idx)  # 将idx视为一个奇数长的回文串的中间字符
        # 偶数长
        l2, r2 = expandCheck(s, idx, idx + 1)  # 将idx，idx+1视为一个偶数长的回文串的中间两个字符
        print(l1,r1,l2,r2)
        if r1 - l1 >= r2 - l2 and r1-l1+1 >= len(res):
            res = s[l1:r1+1]
        if r1 - l1 < r2 - l2 and r2-l2+1 > len(res):
            res = s[l2:r2+1]
        # print(res)
    return res

print(longestPalindrome5("cbbd"))


            

