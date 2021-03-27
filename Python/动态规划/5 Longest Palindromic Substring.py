"""
solution 2
动态规划-超时

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
        for i in range(n):  # i表示子串起始的下标
            j = i + L
            if j >= n:  # 注意边界条件
                break
            if L == 0:
                # 子串长度为0，故i == j
                dp_table[i][j] = True
            elif L == 1:  # 子串长度为 1，值为s[j] == s[i]
                dp_table[i][j] = (s[j] == s[i])
            else:
                # 取决于上一个状态与当前索引的值是否相同
                dp_table[i][j] = (dp_table[i + 1][j - 1] and s[i] == s[j])
            if dp_table[i][j] and L + 1 > len(ans):  # s[i:j+1]是回文并且长度更大
                ans = s[i:j+1]
            # print(dp_table)
            # print(ans)
    return ans