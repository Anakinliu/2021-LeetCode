# 最长公共前缀
def longestCommonPrefix(strs):
    longest_idx = 0
    idx = 0
    s_len = len(strs)
    while idx < s_len:
        if idx + 1 < s_len:
            cur = strs[idx]
            nxt = strs[idx+1]
            for idx,(a,b) in zip(cir, nxt):
                if idx >a == b:

