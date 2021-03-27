# 最长公共前缀
def longestCommonPrefix(strs):
    s_len = len(strs)

    if s_len == 0:
        return ""
    if s_len == 1:
        return strs[0]

    longest = ""
    idx = 1
    max_len = 0
    while idx < s_len:

        cur = strs[idx]
        pre = strs[idx-1]
        i_max = 0
        for a,b in zip(cur, pre):
            if a == b:
                i_max += 1
            else:
                i_max = 0
                break
        if idx <= 1:  # 前两个的最长公共子串就限制了所有后面的元素的最长公共子串
            max_len = i_max

        longest = cur[:max_len] if i_max > max_len else cur[:i_max]
        if longest == "":
            break
        idx += 1
    return longest

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["flower","flow"]))
print(longestCommonPrefix(["dog","racecar","car"]))
print(longestCommonPrefix(["dog"]))
print(longestCommonPrefix(["dog","racecar"]))
print(longestCommonPrefix(["ca","c","bba","bacb","bcb"]))
