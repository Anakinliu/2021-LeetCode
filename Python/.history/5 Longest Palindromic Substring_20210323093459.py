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
solution 2
动态规划

在状态转移方程中，我们是从长度较短的字符串向长度较长的字符串进行转移的，
因此一定要注意动态规划的循环顺序。
"""
def longestPalindrome4(s):
    n = len(s)
    # n * n 的二维的数组
    dp_table = [[False] * n for _ in range(n)]
    # dp_table[i][j] 表示 s[i:j+1] 是否为回文
    # print(dp_table)
    ans = ""
    for L in range(n):  # L表示子串长度
        for i in range(n):  # i表示子串 的下表
            j = i + L
            if j >= n:  # 注意边界条件
                break
            if L == 0:
                # 此时 L == 0，故i == j
                dp_table[i][j] = True
            elif L == 1:
                dp_table[i][j] = (s[j] == s[i])
            else:
                # 取决于上一个状态
                dp_table[i][j] = (dp_table[i + 1][j - 1] and s[i] == s[j])
            if dp_table[i][j] and L + 1 > len(ans):  # s[i:j+1]是回文并且长度更大
                ans = s[i:j+1]
            # print(dp_table)
            # print(ans)
    return ans

"""
solution 3

中心扩展算法
"""
def longestPalindrome5(s):
    res = s[0]

    # 最大可扩展长度
    def expandCheck(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1
        
    for idx in range(len(s)):  # 从第一个字符开始枚举
        l1, r1 = expandCheck(s, idx, idx)  # 将idx视为一个奇数长的回文串的中间字符
        l2, r2 = expandCheck(s, idx, idx + 1)  # 将idx，idx+1视为一个偶数长的回文串的中间两个字符
        if r1 - l1 > r2 - l2 and r1-l1+1 > len(res):
            res = s[l1:r1+1]
        if r1 - l1 < r2 - l2 and r2-l2+1 > len(res):
            res = s[l2:r2+1]
        print(res)
    return res

print(longestPalindrome5("cbbd"))


            

