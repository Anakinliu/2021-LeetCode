# 最长公共前缀
def longestCommonPrefix(strs):
    if not strs:
        return ""
    s_len = len(strs)
    point = strs[0]  # 以第一个为标准
    for s in strs[1:]:
        lst = []
        for a,b in zip(s, point):
            if a == b:
                lst.append(a)
            else:
                break
        point = ''.join(lst)

    return point

print(longestCommonPrefix(["flower","flow","flight"]))
# print(longestCommonPrefix(["flower","flow"]))
# print(longestCommonPrefix(["dog","racecar","car"]))
# print(longestCommonPrefix(["dog"]))
# print(longestCommonPrefix(["dog","racecar"]))
print(longestCommonPrefix(["ca","c","bba","bacb","bcb"]))
