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
        for i, (a,b) in enumerate(zip(cur, pre)):
            if a == b:
                i_max += 1
            else:
                break
        if 
        longest = cur[:i_max]

        idx += 1
    return longest

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["flower","flow"]))
# print(longestCommonPrefix(["dog","racecar","car"]))
# print(longestCommonPrefix(["dog"]))
# print(longestCommonPrefix(["dog","racecar"]))
