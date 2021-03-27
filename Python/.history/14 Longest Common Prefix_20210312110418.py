# 最长公共前缀
def longestCommonPrefix(strs):
    if not strs:
        return ""
    s_len = len(strs)
    point = strs[0]  # 以第一个为标准
    for s in strs[1:]:
        idx = 0
        for a,b in zip(s, point):
            if a == b:
                idx += 1
            else:
                break
        point = point[:idx]

    return point

# @
def longestCommonPrefix2(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ""
    shortest = min(strs,key=len)
    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
    return shortest 

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["flower","flow"]))
print(longestCommonPrefix(["dog","racecar","car"]))
print(longestCommonPrefix(["dog"]))
print(longestCommonPrefix(["dog","racecar"]))
print(longestCommonPrefix(["ca","c","bba","bacb","bcb"]))
print(longestCommonPrefix2(["aaab","acbd","aaa"]))
