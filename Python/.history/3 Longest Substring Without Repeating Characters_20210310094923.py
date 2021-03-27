def lengthOfLongestSubstring(s):
    s_len = len(s)
    for i in range(s_len):
        for j in range(i+s_len):
