# 最长公共前缀
def longestCommonPrefix(strs):
    longest = ""
    idx = 0
    s_len = len(strs)
    while idx < s_len:
        if idx + 1 < s_len:
            cur = strs[idx]
            nxt = strs[idx+1]
            for i,(a,b) in enumerate(zip(cur, nxt)):
                if a != b:
                    longest = cur[:i]
                    break
            
