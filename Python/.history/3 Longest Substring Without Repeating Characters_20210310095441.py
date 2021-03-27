# 我只会暴力方法
def lengthOfLongestSubstring(s):
    s_len = len(s)
    max_len = 0
    for i in range(s_len):
        ss = set(s[i])
        count = 1
        for j in range(i+1, s_len):
            if s[j] in ss:
                break
            else:
                count += 1
                ss.add(s[j])
        max_len = max(max_len, count)
    return max_len




print(lengthOfLongestSubstring('abbcder'))
