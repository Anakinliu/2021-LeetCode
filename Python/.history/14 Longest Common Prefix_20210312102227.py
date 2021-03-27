# 最长公共前缀
def longestCommonPrefix(strs):
    longest = ""
    idx = 1
    s_len = len(strs)

    if s_len == 0:
        return ""
    if s_len == 1:
        return strs[0]
        
    while idx < s_len:
        if strs[idx].startwith(longest):
            cur = strs[idx]
            pre = strs[idx-1]
            for i,(a,b) in enumerate(zip(cur, nxt)):
                if a != b:
                    longest = cur[:i]
                    break
    return longest
            
