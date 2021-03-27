# 最长公共前缀
def longestCommonPrefix(strs):
    s_len = len(strs)

    if s_len == 0:
        return ""
    if s_len == 1:
        return strs[0]

    longest = ""
    idx = 1
    while idx < s_len:
        if strs[idx].startwith(longest):
            cur = strs[idx]
            pre = strs[idx-1]
            for i,(a,b) in enumerate(zip(cur, pre)):
                if a != b:
                    longest = cur[:i]
                    break
        else:
            break
    return longest

print(longestCommonPrefix(["flower","flow","flight"]))
