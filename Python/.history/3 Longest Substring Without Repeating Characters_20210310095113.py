def lengthOfLongestSubstring(s):
    s_len = len(s)
    for i in range(s_len):
        s = set(i)
        count = 1
        for j in range(i+1, s_len):
            if j in s:
                break
            else:
                count += 1
                s.add(j)