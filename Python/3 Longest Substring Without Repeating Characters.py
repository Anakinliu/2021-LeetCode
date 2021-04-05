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
    used = {}  # key为 s 中的字符，value为出现的位置
    max_length = start = 0  # start:无重复子串的起始索引
    for i, c in enumerate(s):
        # 出现重复的了
        if c in used and start <= used[c]:
            start = used[c] + 1  
        else:  # 没有重复的，则最大长度可以增加了
            max_length = max(max_length, i - start + 1)
        used[c] = i
    
    return max_length


print(lengthOfLongestSubstring2('abbcder'))
