# 最长回文子串,1 <= s.length <= 1000
# 我的暴力解法
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
            if isPal(s[i:j+1], n):
                if n > max_len:
                    max_len = n
                    res =
    return max_len

# print(longestPalindrome("babad"))
print(longestPalindrome("ac"))
            
            

