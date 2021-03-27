# 最长公共前缀
def longestCommonPrefix(strs):
    if not strs:
        return ""
    s_len = len(strs)
    point = strs[0]  # 以第一个为 
    for s in strs[1:]:



    return longest

print(longestCommonPrefix(["flower","flow","flight"]))
# print(longestCommonPrefix(["flower","flow"]))
# print(longestCommonPrefix(["dog","racecar","car"]))
# print(longestCommonPrefix(["dog"]))
# print(longestCommonPrefix(["dog","racecar"]))
print(longestCommonPrefix(["ca","c","bba","bacb","bcb"]))
