def lengthOfLongestSubstring(s):
    s_len = len(s)
    for i in range(s_len):
        s = set(i)
        for j in range(i+1, s_len):
