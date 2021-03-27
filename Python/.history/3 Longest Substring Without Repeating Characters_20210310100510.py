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

# @motal
def lengthOfLongestSubstring2(s):
    used = {}
    max_length = start = 0
    for i, c in enumerate(s):
        if c in used and start <= used[c]:
            start = used[c] + 1
        else:
            max_length = max(max_length, i - start + 1)
        used[c] = i
    
    return max_length


print(lengthOfLongestSubstring('abbcder'))
