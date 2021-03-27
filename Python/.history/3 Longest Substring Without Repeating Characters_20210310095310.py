def lengthOfLongestSubstring(s):
    s_len = len(s)
    max_len = 0
    for i in range(s_len):
        s = set(s[i])
        count = 1
        for j in range(i+1, s_len):
            if s[j] in s:
                break
            else:
                count += 1
                s.add(s[j])
        max_len = max(max_len, count)
    return max_len

print(lengthOfLongestSubstring('ab'))
